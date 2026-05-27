import pytest

from pages.bookstore.book_store_page import BookStorePage


@pytest.mark.bookstore
def test_book_list_loads(page, step_logger):
    store = BookStorePage(page)
    step_logger.log_step("Open Book Store page")
    store.open()
    titles = store.visible_book_titles()
    assert len(titles) > 0
    step_logger.log_pass(f"Book list shows {len(titles)} titles")


@pytest.mark.bookstore
def test_book_search(page, step_logger):
    store = BookStorePage(page)
    store.open()
    step_logger.log_step("Search for 'Git'")
    store.search("Git")
    store.assert_search_result("Git")
    step_logger.log_pass("Search returned results containing 'Git'")


@pytest.mark.bookstore
def test_book_search_no_results(page, step_logger):
    store = BookStorePage(page)
    store.open()
    step_logger.log_step("Search for a term with no matches")
    store.search("zzznomatch999")
    titles = store.visible_book_titles()
    assert len(titles) == 0
    step_logger.log_pass("No results returned for unmatched query")
