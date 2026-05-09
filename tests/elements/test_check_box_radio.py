import pytest

from pages.elements.check_box_page import CheckBoxPage
from pages.elements.radio_button_page import RadioButtonPage


@pytest.mark.elements
def test_checkbox_expand_and_select(page, step_logger):
    cb = CheckBoxPage(page)
    step_logger.log_step("Open CheckBox page")
    cb.open()

    step_logger.log_step("Expand all items")
    cb.expand_all()

    step_logger.log_step("Select 'Desktop' node")
    cb.select_item("Desktop")

    step_logger.log_step("Verify 'desktop' appears in result")
    cb.assert_item_checked("desktop")
    step_logger.log_pass("CheckBox tree expand and select verified")


@pytest.mark.elements
def test_checkbox_home_selects_all(page, step_logger):
    cb = CheckBoxPage(page)
    step_logger.log_step("Open CheckBox page and select Home (root)")
    cb.open()
    cb.select_item("Home")
    checked = cb.checked_items()
    step_logger.log_step(f"Checked items: {checked}")
    assert len(checked) > 0
    step_logger.log_pass("Selecting Home checked multiple items")


@pytest.mark.elements
def test_radio_yes(page, step_logger):
    rb = RadioButtonPage(page)
    step_logger.log_step("Open Radio Button page")
    rb.open()

    step_logger.log_step("Click 'Yes' radio")
    rb.click_yes()
    rb.assert_selected("Yes")
    step_logger.log_pass("'Yes' radio selection confirmed")


@pytest.mark.elements
def test_radio_impressive(page, step_logger):
    rb = RadioButtonPage(page)
    rb.open()
    step_logger.log_step("Click 'Impressive' radio")
    rb.click_impressive()
    rb.assert_selected("Impressive")
    step_logger.log_pass("'Impressive' radio selection confirmed")


@pytest.mark.elements
def test_radio_no_is_disabled(page, step_logger):
    rb = RadioButtonPage(page)
    rb.open()
    step_logger.log_step("Assert 'No' radio is disabled")
    rb.assert_no_disabled()
    step_logger.log_pass("'No' radio confirmed disabled")
