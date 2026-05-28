"""API-level tests against /Account/v1 and /BookStore/v1/Books."""
import pytest


@pytest.mark.bookstore
def test_api_generate_token(api_context, bookstore_user):
    resp = api_context.post(
        "/Account/v1/GenerateToken",
        data={
            "userName": bookstore_user["username"],
            "password": bookstore_user["password"],
        },
    )
    assert resp.status == 200
    body = resp.json()
    assert body.get("token") is not None
    assert body.get("status") == "Success"


@pytest.mark.bookstore
def test_api_authorized(api_context, bookstore_user):
    resp = api_context.post(
        "/Account/v1/Authorized",
        data={
            "userName": bookstore_user["username"],
            "password": bookstore_user["password"],
        },
    )
    assert resp.status == 200
    assert resp.json() is True


@pytest.mark.bookstore
def test_api_books_list(api_context):
    resp = api_context.get("/BookStore/v1/Books")
    assert resp.status == 200
    body = resp.json()
    books = body.get("books", [])
    assert len(books) > 0


@pytest.mark.bookstore
def test_api_books_have_required_fields(api_context):
    resp = api_context.get("/BookStore/v1/Books")
    books = resp.json().get("books", [])
    required = {"isbn", "title", "subTitle", "author"}
    for book in books:
        missing = required - book.keys()
        assert not missing, f"Book missing fields: {missing}"


@pytest.mark.bookstore
def test_api_user_profile(api_context, bookstore_user):
    # Generate token first
    token_resp = api_context.post(
        "/Account/v1/GenerateToken",
        data={
            "userName": bookstore_user["username"],
            "password": bookstore_user["password"],
        },
    )
    token = token_resp.json()["token"]

    # Get user ID
    user_resp = api_context.post(
        "/Account/v1/Authorized",
        data={
            "userName": bookstore_user["username"],
            "password": bookstore_user["password"],
        },
    )
    assert user_resp.status == 200
