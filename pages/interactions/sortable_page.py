from playwright.sync_api import Page, expect

from core.base_page import BasePage


class SortablePage(BasePage):
    URL = "sortable"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.list_tab = page.locator("#demo-tab-list")
        self.grid_tab = page.locator("#demo-tab-grid")
        self.list_items = page.locator("#demo-tabpane-list .list-group-item")

    def open(self) -> None:
        self.navigate(self.URL)

    def get_list_order(self) -> list[str]:
        return self.list_items.all_inner_texts()

    def drag_item_to(self, source_text: str, target_text: str) -> None:
        source = self.page.locator(
            "#demo-tabpane-list .list-group-item", has_text=source_text
        )
        target = self.page.locator(
            "#demo-tabpane-list .list-group-item", has_text=target_text
        )
        source.drag_to(target)
