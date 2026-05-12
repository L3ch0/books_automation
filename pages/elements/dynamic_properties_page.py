from playwright.sync_api import Page, expect

from core.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    URL = "dynamic-properties"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.enable_after_btn = page.locator("#enableAfter")
        self.color_change_btn = page.locator("#colorChange")
        self.visible_after_btn = page.locator("#visibleAfter")

    def open(self) -> None:
        self.navigate(self.URL)

    def wait_for_button_enabled(self, timeout: int = 6_000) -> None:
        expect(self.enable_after_btn).to_be_enabled(timeout=timeout)

    def wait_for_button_visible(self, timeout: int = 6_000) -> None:
        expect(self.visible_after_btn).to_be_visible(timeout=timeout)

    def assert_color_changed(self) -> None:
        # Button gains text-danger class after ~5 s.
        expect(self.color_change_btn).to_have_class(
            "mt-4 text-danger btn btn-primary", timeout=6_000
        )
