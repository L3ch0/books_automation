import pytest

from pages.elements.web_tables_page import WebTablesPage


@pytest.mark.elements
def test_add_record(page, step_logger):
    wt = WebTablesPage(page)
    step_logger.log_step("Open Web Tables page")
    wt.open()

    step_logger.log_step("Add new record for 'TestUser'")
    wt.add_record("Test", "User", "test@tables.com", "30", "50000", "QA")

    step_logger.log_step("Assert new row appears in table")
    wt.assert_row_contains("TestUser" if False else "Test")
    step_logger.log_pass("Record added and verified")


@pytest.mark.elements
def test_search_record(page, step_logger):
    wt = WebTablesPage(page)
    wt.open()
    step_logger.log_step("Search for 'Cierra'")
    wt.search("Cierra")
    wt.assert_row_contains("Cierra")
    step_logger.log_pass("Search returned expected row")


@pytest.mark.elements
def test_delete_record(page, step_logger):
    wt = WebTablesPage(page)
    wt.open()
    step_logger.log_step("Delete first row (Cierra Vega)")
    wt.delete_row(1)
    wt.assert_row_absent("Cierra Vega")
    step_logger.log_pass("Row deleted and no longer visible")


@pytest.mark.elements
def test_edit_record(page, step_logger):
    wt = WebTablesPage(page)
    wt.open()
    step_logger.log_step("Edit first record")
    wt.edit_row(1)
    # Update salary
    wt.fill(wt.salary_input, "99999")
    wt.click(wt.submit_btn)
    wt.assert_row_contains("99999")
    step_logger.log_pass("Row edited with new salary")
