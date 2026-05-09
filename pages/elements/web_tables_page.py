from playwright.sync_api import Page, expect

from core.base_page import BasePage


class WebTablesPage(BasePage):
    URL = "webtables"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.add_btn = page.locator("#addNewRecordButton")
        self.search_box = page.locator("#searchBox")
        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.email_input = page.locator("#userEmail")
        self.age_input = page.locator("#age")
        self.salary_input = page.locator("#salary")
        self.department_input = page.locator("#department")
        self.submit_btn = page.locator("#submit")
        self.table_rows = page.locator(".rt-tbody .rt-tr-group")

    def open(self) -> None:
        self.navigate(self.URL)

    def add_record(self, first: str, last: str, email: str, age: str, salary: str, dept: str) -> None:
        self.click(self.add_btn)
        self.fill(self.first_name_input, first)
        self.fill(self.last_name_input, last)
        self.fill(self.email_input, email)
        self.fill(self.age_input, age)
        self.fill(self.salary_input, salary)
        self.fill(self.department_input, dept)
        self.click(self.submit_btn)

    def search(self, term: str) -> None:
        self.fill(self.search_box, term)

    def delete_row(self, row_index: int) -> None:
        delete_btn = self.page.locator(f"[id^='delete-record-{row_index}']")
        self.click(delete_btn)

    def edit_row(self, row_index: int) -> None:
        edit_btn = self.page.locator(f"[id^='edit-record-{row_index}']")
        self.click(edit_btn)

    def assert_row_contains(self, text: str) -> None:
        expect(self.page.locator(".rt-tbody")).to_contain_text(text)

    def assert_row_absent(self, text: str) -> None:
        expect(self.page.locator(".rt-tbody")).not_to_contain_text(text)
