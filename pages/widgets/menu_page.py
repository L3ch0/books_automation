from playwright.sync_api import Page, expect

from core.base_page import BasePage


class MenuPage(BasePage):
    URL = "menu"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.main_items = page.locator("#nav-menu > li > a")

    def open(self) -> None:
        self.navigate(self.URL)

    def hover_main_item(self, name: str) -> None:
        item = self.page.locator("#nav-menu > li > a", has_text=name)
        item.hover()

    def click_sub_item(self, name: str) -> None:
        item = self.page.locator("#nav-menu a", has_text=name)
        self.scroll_into_view(item)
        item.hover()
        item.click()

    def assert_main_items_count(self, count: int) -> None:
        expect(self.main_items).to_have_count(count)
