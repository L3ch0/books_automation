"""Data-driven regression suite exercising key flows with factory data."""
import pytest

from pages.elements.text_box_page import TextBoxPage
from pages.elements.web_tables_page import WebTablesPage
from test_data.factories import WEB_TABLE_RECORDS, make_user_record


@pytest.mark.regression
@pytest.mark.elements
@pytest.mark.parametrize("record", WEB_TABLE_RECORDS)
def test_web_table_add_factory_record(page, step_logger, record):
    wt = WebTablesPage(page)
    step_logger.log_step(f"Add record: {record.first_name} / {record.department}")
    wt.open()
    wt.add_record(
        record.first_name,
        record.last_name,
        record.email,
        record.age,
        record.salary,
        record.department,
    )
    wt.assert_row_contains(record.first_name)
    step_logger.log_pass(f"Record '{record.first_name}' added and verified")


@pytest.mark.regression
@pytest.mark.elements
@pytest.mark.parametrize("name,email", [
    ("Carol White", "carol@regression.com"),
    ("Dan Black", "dan@regression.com"),
    ("Eve Green", "eve@regression.com"),
])
def test_text_box_regression(page, step_logger, name, email):
    tb = TextBoxPage(page)
    step_logger.log_step(f"Text box regression for {name}")
    tb.open()
    tb.submit_form(name, email, "Regression Rd 1", "Regression Rd 2")
    tb.output_contains(name, email, "Regression Rd 1", "Regression Rd 2")
    step_logger.log_pass(f"Regression passed for {name}")
