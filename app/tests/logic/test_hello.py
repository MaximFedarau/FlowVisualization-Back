from app.routers.hello import get_hello


def test_get_hello() -> None:
    """Test get_hello method."""
    assert get_hello()["message"] == "Hello from router!"
