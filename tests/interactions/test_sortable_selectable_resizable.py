import pytest

from pages.interactions.resizable_page import ResizablePage
from pages.interactions.selectable_page import SelectablePage
from pages.interactions.sortable_page import SortablePage


@pytest.mark.interactions
def test_sortable_reorder(page, step_logger):
    sortable = SortablePage(page)
    step_logger.log_step("Open Sortable page")
    sortable.open()
    initial = sortable.get_list_order()
    step_logger.log_step(f"Initial order: {initial[:3]}")
    step_logger.log_step("Drag first item to second position")
    sortable.drag_item_to(initial[0], initial[1])
    new_order = sortable.get_list_order()
    assert new_order != initial
    step_logger.log_pass("List order changed after drag")


@pytest.mark.interactions
def test_selectable_items(page, step_logger):
    selectable = SelectablePage(page)
    step_logger.log_step("Open Selectable page")
    selectable.open()
    step_logger.log_step("Click 'Cras justo odio' list item")
    selectable.click_list_item("Cras justo odio")
    selectable.assert_item_active("Cras justo odio")
    step_logger.log_step("Click 'Dapibus ac facilisis in' list item")
    selectable.click_list_item("Dapibus ac facilisis in")
    assert selectable.count_active() == 2
    step_logger.log_pass("Two items selected")


@pytest.mark.interactions
def test_resizable_within_bounds(page, step_logger):
    resizable = ResizablePage(page)
    step_logger.log_step("Open Resizable page")
    resizable.open()
    before = resizable.get_box_size()
    step_logger.log_step(f"Initial size: {before}")
    step_logger.log_step("Resize box by 50x50 px")
    resizable.resize_restricted_box(50, 50)
    after = resizable.get_box_size()
    step_logger.log_step(f"New size: {after}")
    assert after["width"] >= before["width"]
    step_logger.log_pass("Box resized successfully")
