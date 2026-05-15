from playwright.sync_api import Page, expect

from core.base_page import BasePage


class AlertsPage(BasePage):
    URL = "alerts"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.alert_btn = page.locator("#alertButton")
        self.timer_alert_btn = page.locator("#timerAlertButton")
        self.confirm_btn = page.locator("#confirmButton")
        self.prompt_btn = page.locator("#promtButton")
        self.confirm_result = page.locator("#confirmResult")
        self.prompt_result = page.locator("#promptResult")

    def open(self) -> None:
        self.navigate(self.URL)

    def click_alert(self) -> str:
        with self.page.expect_event("dialog") as dialog_info:
            self.click(self.alert_btn)
        dialog = dialog_info.value
        msg = dialog.message
        dialog.accept()
        return msg

    def click_timer_alert(self, timeout: int = 7_000) -> str:
        with self.page.expect_event("dialog", timeout=timeout) as dialog_info:
            self.click(self.timer_alert_btn)
        dialog = dialog_info.value
        msg = dialog.message
        dialog.accept()
        return msg

    def click_confirm_accept(self) -> None:
        with self.page.expect_event("dialog") as dialog_info:
            self.click(self.confirm_btn)
        dialog_info.value.accept()

    def click_confirm_dismiss(self) -> None:
        with self.page.expect_event("dialog") as dialog_info:
            self.click(self.confirm_btn)
        dialog_info.value.dismiss()

    def click_prompt(self, text: str) -> None:
        with self.page.expect_event("dialog") as dialog_info:
            self.click(self.prompt_btn)
        dialog_info.value.accept(text)

    def assert_confirm_result(self, text: str) -> None:
        expect(self.confirm_result).to_have_text(text)

    def assert_prompt_result(self, text: str) -> None:
        expect(self.prompt_result).to_contain_text(text)
