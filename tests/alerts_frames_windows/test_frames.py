import pytest

from pages.alerts_frames_windows.frames_page import FramesPage, NestedFramesPage


@pytest.mark.alerts
def test_frame1_text(page, step_logger):
    frames = FramesPage(page)
    step_logger.log_step("Open Frames page")
    frames.open()
    step_logger.log_step("Read text from frame1")
    text = frames.text_in_frame("frame1")
    assert text == "This is a sample page"
    step_logger.log_pass(f"Frame1 text: '{text}'")


@pytest.mark.alerts
def test_frame2_text(page, step_logger):
    frames = FramesPage(page)
    frames.open()
    step_logger.log_step("Read text from frame2")
    text = frames.text_in_frame("frame2")
    assert text == "This is a sample page"
    step_logger.log_pass(f"Frame2 text: '{text}'")


@pytest.mark.alerts
def test_nested_frames(page, step_logger):
    nested = NestedFramesPage(page)
    step_logger.log_step("Open Nested Frames page")
    nested.open()
    step_logger.log_step("Read parent frame text")
    parent_text = nested.parent_frame_text()
    assert "Parent frame" in parent_text
    step_logger.log_step("Read child frame text")
    child_text = nested.child_frame_text()
    assert "Child Iframe" in child_text
    step_logger.log_pass("Nested frame texts verified")
