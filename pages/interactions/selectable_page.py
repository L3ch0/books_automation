from playwright.sync_api import Page, expect

from core.base_page import BasePage


class SelectablePage(BasePage):
    URL = "selectable"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.list_tab = page.locator("#demo-tab-list")
        self.list_items = page.locator("#demo-tabpane-list .list-group-item")
        self.active_items = page.locator(
            "#demo-tabpane-list .list-group-item.active"
        )

    def open(self) -> None:
        self.navigate(self.URL)

    def click_list_item(self, text: str) -> None:
        item = self.page.locator(
            "#demo-tabpane-list .list-group-item", has_text=text
        )
        self.click(item)

    def assert_item_active(self, text: str) -> None:
        item = self.page.locator(
            "#demo-tabpane-list .list-group-item.active", has_text=text
        )
        expect(item).to_be_visible()

    def count_active(self) -> int:
        return self.active_items.count()
