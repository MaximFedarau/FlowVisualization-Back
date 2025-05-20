from fastapi import FastAPI

from app.routers import (
    hello,
    post_dinic_visualization,
    post_edmonds_karp_visualization,
    post_ford_fullkerson_visualization,
    post_layered_flow,
    post_random_flow,
    video_generation,
)

app = FastAPI()


app.include_router(post_random_flow.router, prefix="/flow", tags=["flow"])
app.include_router(post_layered_flow.router,
                   prefix="/flow/layered", tags=["flow"])
app.include_router(hello.router, prefix="/api")
app.include_router(video_generation.router, prefix="/video", tags=["video"])
app.include_router(
    post_ford_fullkerson_visualization.router,
    prefix="/ford-fullkerson",
    tags=["visualization"],
)
app.include_router(
    post_edmonds_karp_visualization.router,
    prefix="/edmonds-karp",
    tags=["visualization"],
)
app.include_router(
    post_dinic_visualization.router,
    prefix="/dinic",
    tags=["visualization"],
)
