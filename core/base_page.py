from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, path: str = "") -> None:
        from config.settings import BASE_URL
        self.page.goto(f"{BASE_URL}/{path.lstrip('/')}")

    def wait_for_page_load(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")

    def scroll_into_view(self, locator: Locator) -> None:
        locator.scroll_into_view_if_needed()

    def click(self, locator: Locator) -> None:
        self.scroll_into_view(locator)
        try:
            locator.click()
        except Exception:
            # DemoQA ad iframes occasionally sit on top of elements; JS click bypasses them.
            self.js_click(locator)

    def js_click(self, locator: Locator) -> None:
        locator.evaluate("el => el.click()")

    def fill(self, locator: Locator, value: str) -> None:
        self.scroll_into_view(locator)
        locator.fill(value)

    def select_option(self, locator: Locator, value: str) -> None:
        self.scroll_into_view(locator)
        locator.select_option(value)

    def get_text(self, locator: Locator) -> str:
        self.scroll_into_view(locator)
        return locator.inner_text()

    def assert_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()

    def assert_text(self, locator: Locator, text: str) -> None:
        expect(locator).to_have_text(text)

    def assert_contains_text(self, locator: Locator, text: str) -> None:
        expect(locator).to_contain_text(text)

    def wait_for_selector(self, selector: str, timeout: int = 10_000) -> Locator:
        self.page.wait_for_selector(selector, timeout=timeout)
        return self.page.locator(selector)

    def dismiss_ad_overlays(self) -> None:
        # Close any fixed-position ad overlays that may block interactions.
        self.page.evaluate("""
            document.querySelectorAll(
                'iframe[id*="google"], div[id*="ad"], div[class*="ad-"]'
            ).forEach(el => el.remove())
        """)
