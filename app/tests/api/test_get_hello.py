from fastapi import status
from fastapi.testclient import TestClient

from app.routers.hello import get_hello


def test_hello(client: TestClient) -> None:
    """Test hello API."""
    response = client.get("/api/hello")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == get_hello()
