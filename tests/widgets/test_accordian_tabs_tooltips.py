import pytest

from pages.widgets.accordian_page import AccordianPage
from pages.widgets.tabs_page import TabsPage
from pages.widgets.tool_tips_page import ToolTipsPage


@pytest.mark.widgets
def test_accordian_expand_section1(page, step_logger):
    acc = AccordianPage(page)
    step_logger.log_step("Open Accordian page")
    acc.open()
    # Section 1 is open by default; clicking collapses, clicking again expands.
    step_logger.log_step("Collapse section 1")
    acc.toggle_section(1)
    acc.assert_section_hidden(1)
    step_logger.log_step("Expand section 1 again")
    acc.toggle_section(1)
    acc.assert_section_visible(1)
    step_logger.log_pass("Section 1 collapse/expand verified")


@pytest.mark.widgets
def test_accordian_expand_section2(page, step_logger):
    acc = AccordianPage(page)
    acc.open()
    step_logger.log_step("Open section 2")
    acc.toggle_section(2)
    acc.assert_section_visible(2)
    step_logger.log_pass("Section 2 expanded")


@pytest.mark.widgets
def test_tabs_origin(page, step_logger):
    tabs = TabsPage(page)
    step_logger.log_step("Open Tabs page")
    tabs.open()
    step_logger.log_step("Click 'Origin' tab")
    tabs.click_tab("origin")
    tabs.assert_active_contains("Contrary to popular belief")
    step_logger.log_pass("Origin tab content verified")


@pytest.mark.widgets
def test_tooltip_on_button(page, step_logger):
    tt = ToolTipsPage(page)
    step_logger.log_step("Open Tool Tips page")
    tt.open()
    step_logger.log_step("Hover over button to trigger tooltip")
    tt.hover_button()
    text = tt.tooltip_text()
    assert "You hovered over the Button" in text
    step_logger.log_pass(f"Tooltip text: '{text}'")
