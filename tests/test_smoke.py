import pytest

from config.settings import BASE_URL


@pytest.mark.smoke
def test_homepage_loads(page, step_logger):
    step_logger.log_step(f"Navigate to {BASE_URL}")
    page.goto(BASE_URL)
    page.wait_for_load_state("domcontentloaded")
    step_logger.log_step("Assert page title contains 'ToolsQA'")
    assert "ToolsQA" in page.title()
    step_logger.log_pass("Homepage loaded and title verified")


@pytest.mark.smoke
def test_main_sections_visible(page, step_logger):
    step_logger.log_step(f"Navigate to {BASE_URL}")
    page.goto(BASE_URL)
    page.wait_for_load_state("domcontentloaded")
    step_logger.log_step("Assert main category cards are present")
    cards = page.locator(".card.mt-4.top-card")
    assert cards.count() >= 6
    step_logger.log_pass(f"Found {cards.count()} category cards")
