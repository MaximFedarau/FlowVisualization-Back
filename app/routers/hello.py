from fastapi import APIRouter

router = APIRouter()


def get_hello() -> dict:
    """Return hello."""
    return {"message": "Hello from router!"}


@router.get("/hello")
def say_hello() -> dict:
    """Say Hello."""
    return get_hello()
