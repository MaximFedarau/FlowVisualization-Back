from fastapi import FastAPI

from app.routers import hello, post_flow_visualization, post_random_flow, video_generation

app = FastAPI(debug=True)

app.include_router(post_random_flow.router, prefix="/flow", tags=["flow"])
app.include_router(hello.router, prefix="/api")
app.include_router(video_generation.router, prefix="/video", tags=["video"])
app.include_router(
    post_flow_visualization.router,
    prefix="/visualization",
    tags=["visualization"],
)


@app.get("/")
def read_root() -> dict:
    """Read root."""
    return {"Hello": "World"}
