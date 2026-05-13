from pathlib import Path

from playwright.sync_api import Page, expect

from core.base_page import BasePage


class PracticeFormPage(BasePage):
    URL = "automation-practice-form"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.mobile = page.locator("#userNumber")
        self.date_of_birth = page.locator("#dateOfBirthInput")
        self.subjects_input = page.locator("#subjectsInput")
        self.upload_input = page.locator("#uploadPicture")
        self.current_address = page.locator("#currentAddress")
        self.state_select = page.locator("#state")
        self.city_select = page.locator("#city")
        self.submit_btn = page.locator("#submit")
        # Confirmation modal
        self.modal = page.locator(".modal-content")
        self.modal_title = page.locator("#example-modal-sizes-title-lg")
        self.modal_table = page.locator(".table-responsive")
        self.modal_close = page.locator("#closeLargeModal")

    def open(self) -> None:
        self.navigate(self.URL)
        self.dismiss_ad_overlays()

    def fill_name(self, first: str, last: str) -> None:
        self.fill(self.first_name, first)
        self.fill(self.last_name, last)

    def fill_email(self, email: str) -> None:
        self.fill(self.email, email)

    def select_gender(self, gender: str) -> None:
        label = self.page.locator(f"label[for='gender-radio-{_gender_index(gender)}']")
        self.js_click(label)

    def fill_mobile(self, number: str) -> None:
        self.fill(self.mobile, number)

    def set_date_of_birth(self, date_str: str) -> None:
        # Clear via triple-click then type; date-picker accepts MM/DD/YYYY
        self.date_of_birth.triple_click()
        self.date_of_birth.type(date_str)
        self.page.keyboard.press("Escape")

    def add_subject(self, subject: str) -> None:
        self.fill(self.subjects_input, subject)
        self.page.wait_for_selector(".subjects-auto-complete__option", timeout=5_000)
        self.page.locator(".subjects-auto-complete__option").first.click()

    def select_hobby(self, hobby: str) -> None:
        idx = {"Sports": 1, "Reading": 2, "Music": 3}[hobby]
        label = self.page.locator(f"label[for='hobbies-checkbox-{idx}']")
        self.js_click(label)

    def upload_picture(self, path: str | Path) -> None:
        self.upload_input.set_input_files(str(path))

    def fill_address(self, address: str) -> None:
        self.fill(self.current_address, address)

    def select_state(self, state: str) -> None:
        self.scroll_into_view(self.state_select)
        self.state_select.click()
        self.page.locator(f"[id^='react-select'][class*='option']", has_text=state).first.click()

    def select_city(self, city: str) -> None:
        self.scroll_into_view(self.city_select)
        self.city_select.click()
        self.page.locator(f"[id^='react-select'][class*='option']", has_text=city).first.click()

    def submit(self) -> None:
        self.js_click(self.submit_btn)

    def assert_modal_visible(self) -> None:
        expect(self.modal_title).to_have_text("Thanks for submitting the form")

    def assert_modal_contains(self, label: str, value: str) -> None:
        row = self.page.locator(".table-responsive tr", has=self.page.locator("td", has_text=label))
        expect(row).to_contain_text(value)

    def close_modal(self) -> None:
        self.click(self.modal_close)


def _gender_index(gender: str) -> int:
    return {"Male": 1, "Female": 2, "Other": 3}[gender]
