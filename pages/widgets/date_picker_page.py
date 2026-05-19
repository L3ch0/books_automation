from playwright.sync_api import Page, expect

from core.base_page import BasePage


class DatePickerPage(BasePage):
    URL = "date-picker"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.date_input = page.locator("#datePickerMonthYearInput")
        self.datetime_input = page.locator("#dateAndTimePickerInput")

    def open(self) -> None:
        self.navigate(self.URL)

    def set_date(self, date_str: str) -> None:
        """Accepts MM/DD/YYYY format."""
        self.date_input.triple_click()
        self.date_input.fill(date_str)
        self.page.keyboard.press("Enter")

    def get_date_value(self) -> str:
        return self.date_input.input_value()

    def set_datetime(self, month: str, year: str, day: str, time_str: str) -> None:
        self.click(self.datetime_input)
        # Select month
        self.page.locator(".react-datepicker__month-select").select_option(label=month)
        # Select year
        self.page.locator(".react-datepicker__year-select").select_option(label=year)
        # Select day
        self.page.locator(
            f".react-datepicker__day--0{day.zfill(2)}:not(.react-datepicker__day--outside-month)"
        ).first.click()
        # Select time from list
        time_opt = self.page.locator(
            ".react-datepicker__time-list-item", has_text=time_str
        ).first
        self.click(time_opt)
