from playwright.sync_api import Page, expect

from core.base_page import BasePage


class ToolTipsPage(BasePage):
    URL = "tool-tips"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.hover_btn = page.locator("#toolTipButton")
        self.hover_field = page.locator("#toolTipTextField")
        self.hover_contrary = page.locator(
            ".text-center a", has_text="Contrary"
        )
        self.tooltip = page.locator(".tooltip-inner")

    def open(self) -> None:
        self.navigate(self.URL)

    def hover_button(self) -> None:
        self.hover_btn.hover()
        expect(self.tooltip).to_be_visible()

    def hover_text_field(self) -> None:
        self.hover_field.hover()
        expect(self.tooltip).to_be_visible()

    def tooltip_text(self) -> str:
        return self.tooltip.inner_text()
