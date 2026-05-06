import re
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from config.settings import (
    BROWSER,
    HEADLESS,
    SCREENSHOTS_DIR,
    SLOW_MO,
    TRACE_MODE,
    TRACES_DIR,
)
from core.ad_blocker import register_ad_blocker
from core.logger import StepLogger, get_run_dir


# ---------------------------------------------------------------------------
# Playwright lifecycle
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as pw:
        yield pw


@pytest.fixture(scope="session")
def browser(playwright_instance) -> Browser:
    launcher = getattr(playwright_instance, BROWSER)
    b = launcher.launch(headless=HEADLESS, slow_mo=SLOW_MO)
    yield b
    b.close()


@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    ctx = browser.new_context(
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=True,
    )
    register_ad_blocker(ctx)

    if TRACE_MODE in ("always",):
        ctx.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield ctx
    ctx.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    p = context.new_page()
    yield p
    p.close()


# ---------------------------------------------------------------------------
# Step logger
# ---------------------------------------------------------------------------

@pytest.fixture
def step_logger(request) -> StepLogger:
    safe_name = re.sub(r"[^\w\-]", "_", request.node.nodeid)
    logger = StepLogger(safe_name)
    yield logger
    logger.close()


# ---------------------------------------------------------------------------
# Tracing + screenshot on failure
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def _tracing(request, context: BrowserContext):
    if TRACE_MODE in ("always", "on_failure"):
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield

    failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else False
    safe_name = re.sub(r"[^\w\-]", "_", request.node.nodeid)

    if TRACE_MODE == "always" or (TRACE_MODE == "on_failure" and failed):
        trace_path = TRACES_DIR / f"{safe_name}.zip"
        context.tracing.stop(path=str(trace_path))
    elif TRACE_MODE == "on_failure":
        context.tracing.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page_fixture = item.funcargs.get("page")
        logger_fixture = item.funcargs.get("step_logger")

        if page_fixture is not None:
            safe_name = re.sub(r"[^\w\-]", "_", item.nodeid)
            screenshot_path = SCREENSHOTS_DIR / f"{safe_name}.png"
            try:
                page_fixture.screenshot(path=str(screenshot_path))
                if logger_fixture:
                    logger_fixture.log_fail(f"Screenshot saved: {screenshot_path}")
                    trace_path = TRACES_DIR / f"{safe_name}.zip"
                    logger_fixture.log_fail(f"Trace saved: {trace_path}")
                # Attach to pytest-html report
                from pytest_html import extras as html_extras
                extra = getattr(rep, "extra", [])
                extra.append(html_extras.image(str(screenshot_path)))
                rep.extra = extra
            except Exception:
                pass
