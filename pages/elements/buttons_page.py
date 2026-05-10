from playwright.sync_api import Page, expect

from core.base_page import BasePage


class ButtonsPage(BasePage):
    URL = "buttons"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.double_click_btn = page.locator("#doubleClickBtn")
        self.right_click_btn = page.locator("#rightClickBtn")
        # "Click Me" button that responds to dynamic click (not the others)
        self.dynamic_click_btn = page.locator("button", has_text="Click Me").last
        self.double_click_msg = page.locator("#doubleClickMessage")
        self.right_click_msg = page.locator("#rightClickMessage")
        self.dynamic_click_msg = page.locator("#dynamicClickMessage")

    def open(self) -> None:
        self.navigate(self.URL)

    def double_click(self) -> None:
        self.scroll_into_view(self.double_click_btn)
        self.page.dblclick("#doubleClickBtn")

    def right_click(self) -> None:
        self.scroll_into_view(self.right_click_btn)
        self.page.click("#rightClickBtn", button="right")

    def dynamic_click(self) -> None:
        self.click(self.dynamic_click_btn)

    def assert_double_click(self) -> None:
        expect(self.double_click_msg).to_have_text("You have done a double click")

    def assert_right_click(self) -> None:
        expect(self.right_click_msg).to_have_text("You have done a right click")

    def assert_dynamic_click(self) -> None:
        expect(self.dynamic_click_msg).to_have_text("You have done a dynamic click")
