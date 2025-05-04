from fastapi import status
from fastapi.testclient import TestClient


def test_generate_layered_flow_success(client: TestClient) -> None:
    """Test genereater_layered_flow success.

    Args:
        client (TestClient): FastAPI TestClient

    """
    nodes_quantity = 5
    response = client.post(
        "/flow/layered/generate",
        params={
            "n": nodes_quantity,
            "layers": 4,
            "density": 0.5,
        },
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["graph"]["n"] == nodes_quantity
    assert len(data["coordinates"]) == nodes_quantity


def test_generate_layered_flow_n_is_too_small(client: TestClient) -> None:
    """Test generate_layered_flow min n.

    Args:
        client (TestClient): FastAPI TestClient

    """
    response = client.post(
        "/flow/layered/generate",
        params={
            "n": 1,
            "layers": 1,
            "density": 0.5,
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "n should be equal at least 2"


def test_generate_layered_flow_l_is_too_small(client: TestClient) -> None:
    """Test generate_layered_flow min l.

    Args:
        client (TestClient): FastAPI TestClient

    """
    response = client.post(
        "/flow/layered/generate",
        params={
            "n": 4,
            "layers": 1,
            "density": 0.5,
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "l should be equal at least 2"


def test_generate_layered_flow_l_is_bigger_than_n(client: TestClient) -> None:
    """Test generate_layered_flow l is greater than n.

    Args:
        client (TestClient): FastAPI TestClient

    """
    response = client.post(
        "/flow/layered/generate",
        params={
            "n": 4,
            "layers": 5,
            "density": 0.5,
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "l should not exceed n"
