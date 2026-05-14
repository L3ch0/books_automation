import tempfile
from pathlib import Path

import pytest

from pages.forms.practice_form_page import PracticeFormPage


@pytest.mark.forms
def test_practice_form_full_submission(page, step_logger, tmp_path):
    form = PracticeFormPage(page)
    step_logger.log_step("Open Practice Form page")
    form.open()

    step_logger.log_step("Fill first and last name")
    form.fill_name("John", "Doe")

    step_logger.log_step("Fill email and mobile")
    form.fill_email("john.doe@example.com")
    form.fill_mobile("9876543210")

    step_logger.log_step("Select gender: Male")
    form.select_gender("Male")

    step_logger.log_step("Set date of birth: 01/15/1990")
    form.set_date_of_birth("01/15/1990")

    step_logger.log_step("Add subject: Maths")
    form.add_subject("Maths")

    step_logger.log_step("Select hobby: Sports")
    form.select_hobby("Sports")

    step_logger.log_step("Upload picture")
    pic = tmp_path / "photo.jpg"
    pic.write_bytes(b"\xff\xd8\xff\xe0" + b"\x00" * 10)
    form.upload_picture(pic)

    step_logger.log_step("Fill current address")
    form.fill_address("123 Test Street, Automation City")

    step_logger.log_step("Select state: NCR and city: Delhi")
    form.select_state("NCR")
    form.select_city("Delhi")

    step_logger.log_step("Submit form")
    form.submit()

    step_logger.log_step("Assert confirmation modal is visible")
    form.assert_modal_visible()

    step_logger.log_step("Verify submitted data in modal")
    form.assert_modal_contains("Student Name", "John Doe")
    form.assert_modal_contains("Student Email", "john.doe@example.com")
    form.assert_modal_contains("Gender", "Male")
    form.assert_modal_contains("Mobile", "9876543210")
    form.assert_modal_contains("Hobbies", "Sports")
    step_logger.log_pass("All confirmation modal values verified")

    form.close_modal()
