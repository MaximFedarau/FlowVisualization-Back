from fastapi import FastAPI

from app.routers import hello, post_random_flow

app = FastAPI(debug=True)

app.include_router(post_random_flow.router, prefix="/flow", tags=["flow"])
app.include_router(hello.router, prefix="/api")


@app.get("/")
def read_root() -> dict:
    """Read root."""
    return {"Hello": "World"}
