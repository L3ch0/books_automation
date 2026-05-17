from playwright.sync_api import Page, expect

from core.base_page import BasePage


class AccordianPage(BasePage):
    URL = "accordian"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.section1_header = page.locator("#section1Heading")
        self.section2_header = page.locator("#section2Heading")
        self.section3_header = page.locator("#section3Heading")
        self.section1_body = page.locator("#section1Content")
        self.section2_body = page.locator("#section2Content")
        self.section3_body = page.locator("#section3Content")

    def open(self) -> None:
        self.navigate(self.URL)

    def toggle_section(self, n: int) -> None:
        header = getattr(self, f"section{n}_header")
        self.click(header)

    def assert_section_visible(self, n: int) -> None:
        body = getattr(self, f"section{n}_body")
        expect(body).to_be_visible()

    def assert_section_hidden(self, n: int) -> None:
        body = getattr(self, f"section{n}_body")
        expect(body).to_be_hidden()
