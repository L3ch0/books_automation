from playwright.sync_api import Frame, Page, expect

from core.base_page import BasePage


class FramesPage(BasePage):
    URL = "frames"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.navigate(self.URL)

    def _frame(self, frame_id: str) -> Frame:
        frame = self.page.frame(name=frame_id) or self.page.frame_locator(
            f"#{frame_id}"
        ).owner
        if frame is None:
            raise RuntimeError(f"Frame '{frame_id}' not found")
        return frame

    def text_in_frame(self, frame_id: str) -> str:
        frame_locator = self.page.frame_locator(f"#{frame_id}")
        return frame_locator.locator("#sampleHeading").inner_text()


class NestedFramesPage(BasePage):
    URL = "nestedframes"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.navigate(self.URL)

    def parent_frame_text(self) -> str:
        return self.page.frame_locator("#frame1").locator("body").inner_text()

    def child_frame_text(self) -> str:
        return (
            self.page.frame_locator("#frame1")
            .frame_locator("iframe")
            .locator("body")
            .inner_text()
        )
