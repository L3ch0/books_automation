from playwright.sync_api import Page, expect

from core.base_page import BasePage


class BrokenLinksPage(BasePage):
    URL = "broken"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.valid_image = page.locator("img[src='/images/Toolsqa.jpg']")
        self.broken_image = page.locator("img[src='/images/Toolsqa_1.jpg']")
        self.valid_link = page.locator("a", has_text="Click For Valid Link")
        self.broken_link = page.locator("a", has_text="Click For Broken Link")

    def open(self) -> None:
        self.navigate(self.URL)

    def valid_image_loads(self) -> bool:
        return self.page.evaluate(
            "img => img.naturalWidth > 0",
            self.valid_image.element_handle(),
        )

    def broken_image_loads(self) -> bool:
        return self.page.evaluate(
            "img => img.naturalWidth > 0",
            self.broken_image.element_handle(),
        )

    def click_valid_link(self) -> None:
        self.click(self.valid_link)

    def click_broken_link(self) -> None:
        self.click(self.broken_link)
