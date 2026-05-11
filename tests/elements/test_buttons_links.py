import pytest
from playwright.sync_api import expect

from pages.elements.broken_links_page import BrokenLinksPage
from pages.elements.buttons_page import ButtonsPage
from pages.elements.links_page import LinksPage


@pytest.mark.elements
def test_double_click(page, step_logger):
    btn_page = ButtonsPage(page)
    step_logger.log_step("Open Buttons page")
    btn_page.open()
    step_logger.log_step("Perform double click")
    btn_page.double_click()
    btn_page.assert_double_click()
    step_logger.log_pass("Double click message verified")


@pytest.mark.elements
def test_right_click(page, step_logger):
    btn_page = ButtonsPage(page)
    btn_page.open()
    step_logger.log_step("Perform right click")
    btn_page.right_click()
    btn_page.assert_right_click()
    step_logger.log_pass("Right click message verified")


@pytest.mark.elements
def test_dynamic_click(page, step_logger):
    btn_page = ButtonsPage(page)
    btn_page.open()
    step_logger.log_step("Perform dynamic click")
    btn_page.dynamic_click()
    btn_page.assert_dynamic_click()
    step_logger.log_pass("Dynamic click message verified")


@pytest.mark.elements
def test_home_link_new_tab(page, step_logger):
    links = LinksPage(page)
    step_logger.log_step("Open Links page")
    links.open()
    step_logger.log_step("Click home link — expect new tab")
    new_tab = links.click_home_new_tab()
    expect(new_tab).to_have_url(lambda url: "demoqa.com" in url)
    step_logger.log_pass("New tab opened at DemoQA URL")
    new_tab.close()


@pytest.mark.elements
@pytest.mark.parametrize("link_name,status", [
    ("created", 201),
    ("no-content", 204),
    ("bad-request", 400),
    ("unauthorized", 401),
    ("forbidden", 403),
])
def test_api_links_status(page, step_logger, link_name, status):
    links = LinksPage(page)
    links.open()
    step_logger.log_step(f"Click '{link_name}' API link, expect {status}")
    links.click_api_link(link_name)
    links.assert_link_response(status)
    step_logger.log_pass(f"Link response shows {status}")


@pytest.mark.elements
def test_valid_image_loads(page, step_logger):
    broken = BrokenLinksPage(page)
    step_logger.log_step("Open Broken Links page")
    broken.open()
    step_logger.log_step("Check valid image naturalWidth > 0")
    assert broken.valid_image_loads()
    step_logger.log_pass("Valid image loaded")


@pytest.mark.elements
def test_broken_image_not_loaded(page, step_logger):
    broken = BrokenLinksPage(page)
    broken.open()
    step_logger.log_step("Check broken image naturalWidth == 0")
    assert not broken.broken_image_loads()
    step_logger.log_pass("Broken image confirmed not loaded")
