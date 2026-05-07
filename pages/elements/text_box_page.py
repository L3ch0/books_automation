from playwright.sync_api import Page, expect

from core.base_page import BasePage


class TextBoxPage(BasePage):
    URL = "text-box"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.full_name = page.locator("#userName")
        self.email = page.locator("#userEmail")
        self.current_address = page.locator("#currentAddress")
        self.permanent_address = page.locator("#permanentAddress")
        self.submit_btn = page.locator("#submit")
        self.output_name = page.locator("#name")
        self.output_email = page.locator("#email")
        self.output_current = page.locator("#currentAddress.mb-1")
        self.output_permanent = page.locator("#permanentAddress.mb-1")

    def open(self) -> None:
        self.navigate(self.URL)

    def submit_form(self, name: str, email: str, current: str, permanent: str) -> None:
        self.fill(self.full_name, name)
        self.fill(self.email, email)
        self.fill(self.current_address, current)
        self.fill(self.permanent_address, permanent)
        self.click(self.submit_btn)

    def output_contains(self, name: str, email: str, current: str, permanent: str) -> None:
        expect(self.output_name).to_contain_text(name)
        expect(self.output_email).to_contain_text(email)
        expect(self.output_current).to_contain_text(current)
        expect(self.output_permanent).to_contain_text(permanent)
