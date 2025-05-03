from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def say_hello() -> dict:
    """Say Hello."""
    return {"message": "Hello from router!"}
