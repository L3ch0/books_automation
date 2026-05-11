from playwright.sync_api import Page, expect

from core.base_page import BasePage


class LinksPage(BasePage):
    URL = "links"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.home_link = page.locator("#simpleLink")
        self.api_links = {
            "created": page.locator("#created"),
            "no-content": page.locator("#no-content"),
            "moved": page.locator("#moved"),
            "bad-request": page.locator("#bad-request"),
            "unauthorized": page.locator("#unauthorized"),
            "forbidden": page.locator("#forbidden"),
            "invalid-url": page.locator("#invalid-url"),
        }
        self.link_response = page.locator("#linkResponse")

    def open(self) -> None:
        self.navigate(self.URL)

    def click_home_new_tab(self) -> "Page":
        with self.page.context.expect_page() as new_page_info:
            self.click(self.home_link)
        return new_page_info.value

    def click_api_link(self, name: str) -> None:
        self.click(self.api_links[name])

    def assert_link_response(self, status_code: int) -> None:
        expect(self.link_response).to_contain_text(str(status_code))
