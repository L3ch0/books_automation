from playwright.sync_api import Page, expect

from core.base_page import BasePage


class ProgressBarPage(BasePage):
    URL = "progress-bar"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.start_stop_btn = page.locator("#startStopButton")
        self.reset_btn = page.locator("#resetButton")
        self.progress_bar = page.locator("#progressBar .progress-bar")

    def open(self) -> None:
        self.navigate(self.URL)

    def start(self) -> None:
        self.click(self.start_stop_btn)

    def stop(self) -> None:
        self.click(self.start_stop_btn)

    def reset(self) -> None:
        self.click(self.reset_btn)

    def get_value(self) -> int:
        return int(self.progress_bar.get_attribute("aria-valuenow") or 0)

    def wait_until_value(self, value: int, timeout: int = 15_000) -> None:
        expect(self.progress_bar).to_have_attribute(
            "aria-valuenow", str(value), timeout=timeout
        )
