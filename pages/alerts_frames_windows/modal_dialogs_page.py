from playwright.sync_api import Page, expect

from core.base_page import BasePage


class ModalDialogsPage(BasePage):
    URL = "modal-dialogs"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.small_modal_btn = page.locator("#showSmallModal")
        self.large_modal_btn = page.locator("#showLargeModal")
        self.small_modal = page.locator("#example-modal-sizes-title-sm")
        self.large_modal = page.locator("#example-modal-sizes-title-lg")
        self.close_small = page.locator("#closeSmallModal")
        self.close_large = page.locator("#closeLargeModal")

    def open(self) -> None:
        self.navigate(self.URL)

    def open_small_modal(self) -> None:
        self.click(self.small_modal_btn)
        expect(self.small_modal).to_be_visible()

    def close_small_modal(self) -> None:
        self.click(self.close_small)
        expect(self.small_modal).not_to_be_visible()

    def open_large_modal(self) -> None:
        self.click(self.large_modal_btn)
        expect(self.large_modal).to_be_visible()

    def close_large_modal(self) -> None:
        self.click(self.close_large)
        expect(self.large_modal).not_to_be_visible()

    def assert_small_modal_text(self, text: str) -> None:
        expect(self.page.locator(".modal-body p")).to_have_text(text)
