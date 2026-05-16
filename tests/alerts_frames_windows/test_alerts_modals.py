import pytest

from pages.alerts_frames_windows.alerts_page import AlertsPage
from pages.alerts_frames_windows.modal_dialogs_page import ModalDialogsPage


@pytest.mark.alerts
def test_simple_alert(page, step_logger):
    alerts = AlertsPage(page)
    step_logger.log_step("Open Alerts page")
    alerts.open()
    step_logger.log_step("Click alert button and accept")
    msg = alerts.click_alert()
    assert "You clicked a button" in msg
    step_logger.log_pass(f"Alert message: '{msg}'")


@pytest.mark.alerts
def test_timer_alert(page, step_logger):
    alerts = AlertsPage(page)
    alerts.open()
    step_logger.log_step("Click timer alert — fires after 5 s")
    msg = alerts.click_timer_alert(timeout=8_000)
    assert "appear" in msg or "button" in msg
    step_logger.log_pass("Timer alert accepted successfully")


@pytest.mark.alerts
def test_confirm_accept(page, step_logger):
    alerts = AlertsPage(page)
    alerts.open()
    step_logger.log_step("Click confirm and accept")
    alerts.click_confirm_accept()
    alerts.assert_confirm_result("You selected Ok")
    step_logger.log_pass("Confirm accepted — result verified")


@pytest.mark.alerts
def test_confirm_dismiss(page, step_logger):
    alerts = AlertsPage(page)
    alerts.open()
    step_logger.log_step("Click confirm and dismiss")
    alerts.click_confirm_dismiss()
    alerts.assert_confirm_result("You selected Cancel")
    step_logger.log_pass("Confirm dismissed — result verified")


@pytest.mark.alerts
def test_prompt(page, step_logger):
    alerts = AlertsPage(page)
    alerts.open()
    step_logger.log_step("Enter text in prompt dialog")
    alerts.click_prompt("DemoQA Test")
    alerts.assert_prompt_result("DemoQA Test")
    step_logger.log_pass("Prompt result verified")


@pytest.mark.alerts
def test_small_modal(page, step_logger):
    modals = ModalDialogsPage(page)
    step_logger.log_step("Open Modal Dialogs page")
    modals.open()
    step_logger.log_step("Open small modal")
    modals.open_small_modal()
    step_logger.log_step("Close small modal")
    modals.close_small_modal()
    step_logger.log_pass("Small modal opened and closed")


@pytest.mark.alerts
def test_large_modal(page, step_logger):
    modals = ModalDialogsPage(page)
    modals.open()
    step_logger.log_step("Open large modal")
    modals.open_large_modal()
    step_logger.log_step("Close large modal")
    modals.close_large_modal()
    step_logger.log_pass("Large modal opened and closed")
