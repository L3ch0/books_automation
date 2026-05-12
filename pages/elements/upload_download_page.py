from pathlib import Path

from playwright.sync_api import Download, Page, expect

from core.base_page import BasePage


class UploadDownloadPage(BasePage):
    URL = "upload-download"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.download_btn = page.locator("#downloadButton")
        self.upload_input = page.locator("#uploadFile")
        self.upload_result = page.locator("#uploadedFilePath")

    def open(self) -> None:
        self.navigate(self.URL)

    def download_file(self) -> Download:
        with self.page.expect_download() as dl_info:
            self.click(self.download_btn)
        return dl_info.value

    def upload_file(self, file_path: str | Path) -> None:
        self.upload_input.set_input_files(str(file_path))

    def assert_upload_result(self, filename: str) -> None:
        expect(self.upload_result).to_contain_text(filename)
