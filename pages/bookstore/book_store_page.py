from playwright.sync_api import Page, expect

from core.base_page import BasePage


class BookStorePage(BasePage):
    URL = "books"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_input = page.locator("#searchBox")
        self.book_rows = page.locator(".rt-tbody .rt-tr-group")
        self.next_btn = page.locator(".-next button")
        self.prev_btn = page.locator(".-previous button")

    def open(self) -> None:
        self.navigate(self.URL)

    def search(self, term: str) -> None:
        self.fill(self.search_input, term)

    def visible_book_titles(self) -> list[str]:
        title_cells = self.page.locator(
            ".rt-tbody .rt-tr-group .rt-td:nth-child(2) a"
        )
        return [t.inner_text() for t in title_cells.all() if t.inner_text()]

    def go_next_page(self) -> None:
        self.click(self.next_btn)

    def go_prev_page(self) -> None:
        self.click(self.prev_btn)

    def assert_search_result(self, title: str) -> None:
        expect(self.page.locator(".rt-tbody")).to_contain_text(title)


class ProfilePage(BasePage):
    URL = "profile"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.book_rows = page.locator(".rt-tbody .rt-tr-group")
        self.delete_account_btn = page.locator("#submit")
        self.username_display = page.locator("#userName-value")

    def open(self) -> None:
        self.navigate(self.URL)

    def assert_username(self, username: str) -> None:
        expect(self.username_display).to_have_text(username)

    def book_count(self) -> int:
        rows = self.book_rows.all()
        return sum(
            1 for r in rows if r.locator(".rt-td a").count() > 0
        )
