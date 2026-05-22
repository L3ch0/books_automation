from playwright.sync_api import Page, expect

from core.base_page import BasePage


class DroppablePage(BasePage):
    URL = "droppable"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.simple_tab = page.locator("#droppableExample-tab-simple")
        self.accept_tab = page.locator("#droppableExample-tab-accept")
        self.revert_tab = page.locator("#droppableExample-tab-revertable")
        # Simple tab targets
        self.drag_me = page.locator("#draggable")
        self.drop_here = page.locator("#droppable")
        # Accept tab
        self.acceptable = page.locator("#acceptable")
        self.not_acceptable = page.locator("#notAcceptable")
        self.accept_drop = page.locator("#droppableExample-tabpane-accept #droppable")

    def open(self) -> None:
        self.navigate(self.URL)

    def simple_drag_and_drop(self) -> None:
        self.drag_me.drag_to(self.drop_here)

    def assert_dropped(self) -> None:
        expect(self.drop_here.locator("p")).to_have_text("Dropped!")

    def drag_acceptable_to_accept_drop(self) -> None:
        self.click(self.accept_tab)
        self.acceptable.drag_to(self.accept_drop)

    def assert_accept_drop_text(self, text: str) -> None:
        expect(self.accept_drop.locator("p")).to_have_text(text)
