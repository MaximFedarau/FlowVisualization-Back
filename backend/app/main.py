from fastapi import FastAPI

from app.routers import (
    post_edmonds_karp_visualization,
    post_ford_fullkerson_visualization,
    post_random_flow,
)

# from app.routers import post_dinic_visualization

app = FastAPI(debug=True)

app.include_router(post_random_flow.router, prefix="/flow", tags=["flow"])
app.include_router(
    post_ford_fullkerson_visualization.router,
    prefix="/ford-fullkerson",
    tags=["visualization"],
)
app.include_router(
    post_edmonds_karp_visualization.router, prefix="/edmonds-karp", tags=["visualization"]
)
# app.include_router(post_dinic_visualization.router, prefix="/dinic", tags=["visualization"])


@app.get("/")
def read_root():
    return {"Fuck": "World"}
