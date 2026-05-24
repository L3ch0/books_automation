"""Bookstore-scoped fixtures: API-created test user, API request context."""
import uuid

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from config.settings import BASE_URL, BOOKSTORE_PASSWORD, BOOKSTORE_USERNAME

_API_BASE = f"{BASE_URL}"


def _strong_password(base: str) -> str:
    """Ensure DemoQA password policy: 8+ chars, upper, digit, special."""
    return f"{base}A1!"


@pytest.fixture(scope="session")
def api_context(playwright_instance: "Playwright") -> APIRequestContext:
    ctx = playwright_instance.request.new_context(base_url=_API_BASE)
    yield ctx
    ctx.dispose()


@pytest.fixture(scope="session")
def bookstore_user(api_context: APIRequestContext):
    """
    Creates a test user via the Account API once per session.
    Handles 'user already exists' gracefully so reruns don't fail.
    """
    username = BOOKSTORE_USERNAME or f"tqa_{uuid.uuid4().hex[:8]}"
    password = BOOKSTORE_PASSWORD or _strong_password("Demoqa")

    resp = api_context.post(
        "/Account/v1/User",
        data={"userName": username, "password": password},
    )
    body = resp.json()

    if resp.status not in (201, 200) and "User exists" not in body.get("message", ""):
        pytest.skip(f"Could not create bookstore user: {body}")

    return {"username": username, "password": password}
