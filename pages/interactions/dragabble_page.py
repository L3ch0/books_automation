from playwright.sync_api import Page, expect

from core.base_page import BasePage


class DragabblePage(BasePage):
    URL = "dragabble"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.simple_tab = page.locator("#draggableExample-tab-simple")
        self.axis_tab = page.locator("#draggableExample-tab-axisRestricted")
        self.simple_drag = page.locator("#draggableExample-tabpane-simple #dragBox")
        self.x_axis_drag = page.locator("#restrictedX")
        self.y_axis_drag = page.locator("#restrictedY")

    def open(self) -> None:
        self.navigate(self.URL)

    def drag_simple(self, dx: int, dy: int) -> None:
        box = self.simple_drag.bounding_box()
        cx = box["x"] + box["width"] / 2
        cy = box["y"] + box["height"] / 2
        self.page.mouse.move(cx, cy)
        self.page.mouse.down()
        self.page.mouse.move(cx + dx, cy + dy, steps=10)
        self.page.mouse.up()

    def drag_x_axis(self, dx: int) -> None:
        self.click(self.axis_tab)
        box = self.x_axis_drag.bounding_box()
        cx = box["x"] + box["width"] / 2
        cy = box["y"] + box["height"] / 2
        self.page.mouse.move(cx, cy)
        self.page.mouse.down()
        self.page.mouse.move(cx + dx, cy, steps=10)
        self.page.mouse.up()

    def get_position(self, locator) -> dict:
        bb = locator.bounding_box()
        return {"x": bb["x"], "y": bb["y"]}
