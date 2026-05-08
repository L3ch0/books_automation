import pytest

from pages.elements.text_box_page import TextBoxPage


@pytest.mark.elements
def test_text_box_submission(page, step_logger):
    text_box = TextBoxPage(page)
    step_logger.log_step("Open Text Box page")
    text_box.open()

    name = "John Doe"
    email = "john@example.com"
    current = "123 Main St"
    permanent = "456 Oak Ave"

    step_logger.log_step(f"Fill form with name={name}, email={email}")
    text_box.submit_form(name, email, current, permanent)

    step_logger.log_step("Assert output section contains submitted values")
    text_box.output_contains(name, email, current, permanent)
    step_logger.log_pass("All submitted values appear in output")


@pytest.mark.elements
@pytest.mark.parametrize("name,email", [
    ("Alice Smith", "alice@test.com"),
    ("Bob Jones", "bob@test.com"),
])
def test_text_box_parametrized(page, step_logger, name, email):
    text_box = TextBoxPage(page)
    step_logger.log_step(f"Submit form for {name}")
    text_box.open()
    text_box.submit_form(name, email, "100 Test Ln", "200 Sample Rd")
    text_box.output_contains(name, email, "100 Test Ln", "200 Sample Rd")
    step_logger.log_pass(f"Output verified for {name}")
