from playwright.sync_api import Page, expect

from core.base_page import BasePage


class RadioButtonPage(BasePage):
    URL = "radio-button"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.yes_label = page.locator("label[for='yesRadio']")
        self.impressive_label = page.locator("label[for='impressiveRadio']")
        self.no_label = page.locator("label[for='noRadio']")
        self.no_radio = page.locator("#noRadio")
        self.success_text = page.locator(".mt-3 .text-success")

    def open(self) -> None:
        self.navigate(self.URL)

    def click_yes(self) -> None:
        self.click(self.yes_label)

    def click_impressive(self) -> None:
        self.click(self.impressive_label)

    def assert_selected(self, text: str) -> None:
        expect(self.success_text).to_have_text(text)

    def assert_no_disabled(self) -> None:
        expect(self.no_radio).to_be_disabled()
