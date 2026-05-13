import tempfile
from pathlib import Path

import pytest

from pages.elements.dynamic_properties_page import DynamicPropertiesPage
from pages.elements.upload_download_page import UploadDownloadPage


@pytest.mark.elements
def test_file_upload(page, step_logger, tmp_path):
    ul_dl = UploadDownloadPage(page)
    step_logger.log_step("Open Upload/Download page")
    ul_dl.open()

    test_file = tmp_path / "upload_test.txt"
    test_file.write_text("hello demoqa")

    step_logger.log_step(f"Upload file: {test_file.name}")
    ul_dl.upload_file(test_file)
    ul_dl.assert_upload_result("upload_test.txt")
    step_logger.log_pass("Upload result shows correct filename")


@pytest.mark.elements
def test_file_download(page, step_logger, tmp_path):
    ul_dl = UploadDownloadPage(page)
    ul_dl.open()
    step_logger.log_step("Trigger file download")
    download = ul_dl.download_file()
    save_path = tmp_path / download.suggested_filename
    download.save_as(str(save_path))
    assert save_path.exists()
    step_logger.log_pass(f"File downloaded to {save_path}")


@pytest.mark.elements
def test_button_enabled_after_delay(page, step_logger):
    dp = DynamicPropertiesPage(page)
    step_logger.log_step("Open Dynamic Properties page")
    dp.open()
    step_logger.log_step("Wait for 'Enable After' button to become enabled (~5 s)")
    dp.wait_for_button_enabled(timeout=7_000)
    step_logger.log_pass("Button is now enabled")


@pytest.mark.elements
def test_button_visible_after_delay(page, step_logger):
    dp = DynamicPropertiesPage(page)
    dp.open()
    step_logger.log_step("Wait for 'Visible After' button to appear (~5 s)")
    dp.wait_for_button_visible(timeout=7_000)
    step_logger.log_pass("Button is now visible")
