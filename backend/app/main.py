from fastapi import FastAPI
from app.routers import post_random_flow
from app.routers import post_flow_visualization

app = FastAPI(debug=True)

app.include_router(post_random_flow.router, prefix="/flow", tags=["flow"])
app.include_router(post_flow_visualization.router, prefix="/visualization", tags=["visualization"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
