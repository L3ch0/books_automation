import pytest

from pages.widgets.date_picker_page import DatePickerPage
from pages.widgets.progress_bar_page import ProgressBarPage
from pages.widgets.slider_page import SliderPage


@pytest.mark.widgets
def test_date_picker_set_date(page, step_logger):
    dp = DatePickerPage(page)
    step_logger.log_step("Open Date Picker page")
    dp.open()
    step_logger.log_step("Set date to 05/15/2025")
    dp.set_date("05/15/2025")
    value = dp.get_date_value()
    assert "05/15/2025" in value
    step_logger.log_pass(f"Date set to: {value}")


@pytest.mark.widgets
def test_slider_set_value(page, step_logger):
    slider = SliderPage(page)
    step_logger.log_step("Open Slider page")
    slider.open()
    step_logger.log_step("Set slider value to 75")
    slider.set_value(75)
    val = slider.get_value()
    assert val == 75
    step_logger.log_pass(f"Slider value is {val}")


@pytest.mark.widgets
def test_progress_bar_start_stop(page, step_logger):
    pb = ProgressBarPage(page)
    step_logger.log_step("Open Progress Bar page")
    pb.open()
    step_logger.log_step("Start progress bar")
    pb.start()
    # Let it run briefly, then stop
    page.wait_for_timeout(2_000)
    step_logger.log_step("Stop progress bar")
    pb.stop()
    val = pb.get_value()
    assert 0 < val < 100
    step_logger.log_pass(f"Progress bar stopped at {val}%")


@pytest.mark.widgets
def test_progress_bar_reset(page, step_logger):
    pb = ProgressBarPage(page)
    pb.open()
    step_logger.log_step("Run progress to 100% then reset")
    pb.start()
    pb.wait_until_value(100, timeout=20_000)
    pb.reset()
    val = pb.get_value()
    assert val == 0
    step_logger.log_pass("Progress bar reset to 0")
