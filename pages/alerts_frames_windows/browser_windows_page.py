from playwright.sync_api import Page, expect

from core.base_page import BasePage


class BrowserWindowsPage(BasePage):
    URL = "browser-windows"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.new_tab_btn = page.locator("#tabButton")
        self.new_window_btn = page.locator("#windowButton")
        self.new_window_msg_btn = page.locator("#messageWindowButton")

    def open(self) -> None:
        self.navigate(self.URL)

    def open_new_tab(self) -> Page:
        with self.page.context.expect_page() as tab_info:
            self.click(self.new_tab_btn)
        tab = tab_info.value
        tab.wait_for_load_state()
        return tab

    def open_new_window(self) -> Page:
        with self.page.context.expect_page() as win_info:
            self.click(self.new_window_btn)
        win = win_info.value
        win.wait_for_load_state()
        return win

    def assert_new_page_heading(self, new_page: Page, text: str) -> None:
        heading = new_page.locator("#sampleHeading")
        expect(heading).to_have_text(text)
