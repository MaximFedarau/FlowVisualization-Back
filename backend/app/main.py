from fastapi import FastAPI

from app.routers import post_ford_fullkerson_visualization, post_random_flow

app = FastAPI(debug=True)

app.include_router(post_random_flow.router, prefix="/flow", tags=["flow"])
app.include_router(
    post_ford_fullkerson_visualization.router,
    prefix="/visualization/ford-fullkerson",
    tags=["visualization"],
)


@app.get("/")
def read_root():
    return {"Fuck": "World"}
