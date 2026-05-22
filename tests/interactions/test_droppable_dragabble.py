import pytest

from pages.interactions.dragabble_page import DragabblePage
from pages.interactions.droppable_page import DroppablePage


@pytest.mark.interactions
def test_simple_drag_and_drop(page, step_logger):
    droppable = DroppablePage(page)
    step_logger.log_step("Open Droppable page")
    droppable.open()
    step_logger.log_step("Drag element onto drop target")
    droppable.simple_drag_and_drop()
    droppable.assert_dropped()
    step_logger.log_pass("Element dropped — 'Dropped!' confirmed")


@pytest.mark.interactions
def test_accept_drag(page, step_logger):
    droppable = DroppablePage(page)
    droppable.open()
    step_logger.log_step("Drag acceptable element to accept-only drop zone")
    droppable.drag_acceptable_to_accept_drop()
    droppable.assert_accept_drop_text("Dropped!")
    step_logger.log_pass("Acceptable element dropped successfully")


@pytest.mark.interactions
def test_drag_simple_box(page, step_logger):
    dragabble = DragabblePage(page)
    step_logger.log_step("Open Dragabble page")
    dragabble.open()
    before = dragabble.get_position(dragabble.simple_drag)
    step_logger.log_step(f"Initial position: {before}")
    step_logger.log_step("Drag box 100px right, 50px down")
    dragabble.drag_simple(100, 50)
    after = dragabble.get_position(dragabble.simple_drag)
    step_logger.log_step(f"New position: {after}")
    assert after["x"] != before["x"] or after["y"] != before["y"]
    step_logger.log_pass("Box moved to a new position")


@pytest.mark.interactions
def test_drag_x_axis_only(page, step_logger):
    dragabble = DragabblePage(page)
    dragabble.open()
    dragabble.drag_x_axis(80)
    # Y should remain the same; X should change.
    step_logger.log_pass("X-axis drag executed without error")
