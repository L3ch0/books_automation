import pytest

from pages.bookstore.book_store_page import ProfilePage
from pages.bookstore.login_page import LoginPage


@pytest.mark.bookstore
def test_profile_shows_username(page, step_logger, bookstore_user):
    login = LoginPage(page)
    step_logger.log_step("Login to reach profile")
    login.open()
    login.login(bookstore_user["username"], bookstore_user["password"])
    login.assert_logged_in()

    profile = ProfilePage(page)
    step_logger.log_step("Open profile page")
    profile.open()
    step_logger.log_step(f"Assert username '{bookstore_user['username']}' shown")
    profile.assert_username(bookstore_user["username"])
    step_logger.log_pass("Profile page shows correct username")
