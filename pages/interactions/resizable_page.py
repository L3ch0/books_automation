from playwright.sync_api import Page, expect

from core.base_page import BasePage


class ResizablePage(BasePage):
    URL = "resizable"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.box = page.locator("#resizableBoxWithRestriction")
        self.handle = page.locator(
            "#resizableBoxWithRestriction span.react-resizable-handle"
        )
        self.free_box = page.locator("#resizable")
        self.free_handle = page.locator(
            "#resizable span.react-resizable-handle"
        )

    def open(self) -> None:
        self.navigate(self.URL)

    def resize_restricted_box(self, dx: int, dy: int) -> None:
        box = self.handle.bounding_box()
        self.page.mouse.move(box["x"] + 5, box["y"] + 5)
        self.page.mouse.down()
        self.page.mouse.move(box["x"] + 5 + dx, box["y"] + 5 + dy)
        self.page.mouse.up()

    def get_box_size(self) -> dict:
        bb = self.box.bounding_box()
        return {"width": int(bb["width"]), "height": int(bb["height"])}
