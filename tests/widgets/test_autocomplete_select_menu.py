import pytest

from pages.widgets.auto_complete_page import AutoCompletePage
from pages.widgets.select_menu_page import SelectMenuPage


@pytest.mark.widgets
def test_multi_autocomplete(page, step_logger):
    ac = AutoCompletePage(page)
    step_logger.log_step("Open Auto Complete page")
    ac.open()
    step_logger.log_step("Type 'Red' in multi input")
    ac.type_multi("Red")
    ac.assert_multi_contains("Red")
    step_logger.log_step("Type 'Blue' in multi input")
    ac.type_multi("Blue")
    ac.assert_multi_contains("Blue")
    step_logger.log_pass("Multi-autocomplete values added")


@pytest.mark.widgets
def test_single_autocomplete(page, step_logger):
    ac = AutoCompletePage(page)
    ac.open()
    step_logger.log_step("Select 'Green' from single auto-complete")
    ac.type_single("Green")
    ac.assert_single_value("Green")
    step_logger.log_pass("Single auto-complete selection verified")


@pytest.mark.widgets
def test_select_menu_old_style(page, step_logger):
    sm = SelectMenuPage(page)
    step_logger.log_step("Open Select Menu page")
    sm.open()
    step_logger.log_step("Select 'Purple' from old-style select")
    sm.select_old_style("5")  # value="5" corresponds to Purple
    step_logger.log_pass("Old-style select option chosen")
