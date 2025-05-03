from fastapi import FastAPI

from src.routers import hello

app = FastAPI()

app.include_router(hello.router, prefix="/api")


@app.get("/")
def read_root() -> dict:
    """Read root."""
    return {"Hello": "World"}
