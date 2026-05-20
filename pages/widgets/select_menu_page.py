from playwright.sync_api import Page, expect

from core.base_page import BasePage


class SelectMenuPage(BasePage):
    URL = "select-menu"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.select_value = page.locator("#withOptGroup")
        self.select_one = page.locator("#selectOne")
        self.old_style = page.locator("#oldSelectMenu")
        self.multi_select = page.locator("#cars")

    def open(self) -> None:
        self.navigate(self.URL)

    def select_value_option(self, text: str) -> None:
        self.scroll_into_view(self.select_value)
        self.select_value.click()
        self.page.locator(
            "#withOptGroup + div .react-select__option", has_text=text
        ).first.click()

    def select_one_option(self, text: str) -> None:
        self.scroll_into_view(self.select_one)
        self.select_one.click()
        self.page.locator(
            "#selectOne + div .react-select__option", has_text=text
        ).first.click()

    def select_old_style(self, value: str) -> None:
        self.select_option(self.old_style, value)

    def select_multi(self, values: list[str]) -> None:
        for v in values:
            self.old_style.select_option(v)
