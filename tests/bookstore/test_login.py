import pytest

from pages.bookstore.login_page import LoginPage


@pytest.mark.bookstore
@pytest.mark.parametrize("username,password,expect_success", [
    ("valid_user_placeholder", "ValidPass1!", True),
    ("invalid_user_xyz", "wrongpassword", False),
    ("", "nopassword", False),
])
def test_login_parametrized(page, step_logger, bookstore_user, username, password, expect_success):
    # Use the fixture-created user for the 'valid' case
    if expect_success:
        username = bookstore_user["username"]
        password = bookstore_user["password"]

    login = LoginPage(page)
    step_logger.log_step(f"Open login page, attempt login as '{username}'")
    login.open()
    login.login(username, password)

    if expect_success:
        step_logger.log_step("Assert redirect to profile page")
        login.assert_logged_in()
        step_logger.log_pass(f"Login succeeded for user '{username}'")
    else:
        step_logger.log_step("Assert error message visible")
        login.assert_login_error()
        step_logger.log_pass("Login rejected as expected")
