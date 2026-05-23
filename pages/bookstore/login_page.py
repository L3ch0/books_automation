from playwright.sync_api import Page, expect

from core.base_page import BasePage


class LoginPage(BasePage):
    URL = "login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.locator("#userName")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("#login")
        self.error_msg = page.locator("#name")
        self.new_user_btn = page.locator("#newUser")

    def open(self) -> None:
        self.navigate(self.URL)

    def login(self, username: str, password: str) -> None:
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_btn)

    def assert_logged_in(self) -> None:
        expect(self.page).to_have_url(
            lambda url: "profile" in url, timeout=8_000
        )

    def assert_login_error(self) -> None:
        expect(self.error_msg).to_be_visible()
        expect(self.error_msg).to_contain_text("Invalid")

    def click_new_user(self) -> None:
        self.click(self.new_user_btn)


class RegisterPage(BasePage):
    URL = "register"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name = page.locator("#firstname")
        self.last_name = page.locator("#lastname")
        self.username = page.locator("#userName")
        self.password = page.locator("#password")
        self.captcha_btn = page.locator(".recaptcha-checkbox-border")
        self.register_btn = page.locator("#register")
        self.output = page.locator("#output")

    def open(self) -> None:
        self.navigate(self.URL)

    def fill_form(self, first: str, last: str, user: str, pwd: str) -> None:
        self.fill(self.first_name, first)
        self.fill(self.last_name, last)
        self.fill(self.username, user)
        self.fill(self.password, pwd)

    def assert_registration_success(self) -> None:
        expect(self.output).to_contain_text("User Register Successfully")
