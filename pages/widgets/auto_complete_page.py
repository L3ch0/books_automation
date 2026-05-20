from playwright.sync_api import Page, expect

from core.base_page import BasePage


class AutoCompletePage(BasePage):
    URL = "auto-complete"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.multi_input = page.locator("#autoCompleteMultipleInput")
        self.single_input = page.locator("#autoCompleteSingleInput")
        self.multi_value = page.locator(".auto-complete__multi-value__label")
        self.single_value = page.locator(".auto-complete__single-value")

    def open(self) -> None:
        self.navigate(self.URL)

    def type_multi(self, color: str) -> None:
        self.multi_input.type(color)
        self.page.locator(".auto-complete__option", has_text=color).first.click()

    def type_single(self, color: str) -> None:
        self.single_input.type(color)
        self.page.locator(".auto-complete__option", has_text=color).first.click()

    def assert_multi_contains(self, color: str) -> None:
        expect(self.multi_value.filter(has_text=color)).to_be_visible()

    def assert_single_value(self, color: str) -> None:
        expect(self.single_value).to_have_text(color)

    def remove_multi_value(self, color: str) -> None:
        close_btn = self.page.locator(
            ".auto-complete__multi-value",
            has=self.page.locator(".auto-complete__multi-value__label", has_text=color),
        ).locator(".auto-complete__multi-value__remove")
        self.click(close_btn)
