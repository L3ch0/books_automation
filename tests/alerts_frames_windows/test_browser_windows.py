import pytest

from pages.alerts_frames_windows.browser_windows_page import BrowserWindowsPage


@pytest.mark.alerts
def test_new_tab(page, step_logger):
    bw = BrowserWindowsPage(page)
    step_logger.log_step("Open Browser Windows page")
    bw.open()

    step_logger.log_step("Open new tab")
    new_tab = bw.open_new_tab()

    step_logger.log_step("Assert heading in new tab")
    bw.assert_new_page_heading(new_tab, "This is a sample page")
    step_logger.log_pass("New tab heading verified")
    new_tab.close()


@pytest.mark.alerts
def test_new_window(page, step_logger):
    bw = BrowserWindowsPage(page)
    bw.open()
    step_logger.log_step("Open new window")
    new_win = bw.open_new_window()
    bw.assert_new_page_heading(new_win, "This is a sample page")
    step_logger.log_pass("New window heading verified")
    new_win.close()
