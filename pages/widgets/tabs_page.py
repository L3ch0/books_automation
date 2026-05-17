from playwright.sync_api import Page, expect

from core.base_page import BasePage


class TabsPage(BasePage):
    URL = "tabs"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.what_tab = page.locator("#demo-tab-what")
        self.origin_tab = page.locator("#demo-tab-origin")
        self.use_tab = page.locator("#demo-tab-use")
        self.more_tab = page.locator("#demo-tab-more")
        self.active_content = page.locator(".tab-content .tab-pane.active")

    def open(self) -> None:
        self.navigate(self.URL)

    def click_tab(self, name: str) -> None:
        tab = getattr(self, f"{name.lower()}_tab")
        self.click(tab)

    def assert_active_contains(self, text: str) -> None:
        expect(self.active_content).to_contain_text(text)
