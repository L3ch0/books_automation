from playwright.sync_api import Page, expect

from core.base_page import BasePage


class CheckBoxPage(BasePage):
    URL = "checkbox"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.expand_all_btn = page.locator("button[title='Expand all']")
        self.result_display = page.locator(".check-box-tree-wrapper ~ .mt-2")

    def open(self) -> None:
        self.navigate(self.URL)

    def expand_all(self) -> None:
        self.click(self.expand_all_btn)

    def select_item(self, label: str) -> None:
        item = self.page.locator(f".rct-title", has_text=label).first
        self.scroll_into_view(item)
        item.click()

    def checked_items(self) -> list[str]:
        results = self.page.locator(".check-box-tree-wrapper ~ .mt-2 span.text-success")
        return [r.inner_text().lower() for r in results.all()]

    def assert_item_checked(self, label: str) -> None:
        result = self.page.locator(".check-box-tree-wrapper ~ .mt-2")
        expect(result).to_contain_text(label.lower())
