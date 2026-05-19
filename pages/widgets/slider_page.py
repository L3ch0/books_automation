from playwright.sync_api import Page, expect

from core.base_page import BasePage


class SliderPage(BasePage):
    URL = "slider"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.slider = page.locator(".range-slider input[type='range']")
        self.value_display = page.locator("#sliderValue")

    def open(self) -> None:
        self.navigate(self.URL)

    def set_value(self, target: int) -> None:
        current = int(self.slider.input_value())
        diff = target - current
        key = "ArrowRight" if diff > 0 else "ArrowLeft"
        self.click(self.slider)
        for _ in range(abs(diff)):
            self.page.keyboard.press(key)

    def get_value(self) -> int:
        return int(self.value_display.input_value())
