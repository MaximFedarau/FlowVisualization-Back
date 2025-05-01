from fastapi import FastAPI
from app.routers import post_random_flow

app = FastAPI(debug=True)

app.include_router(post_random_flow.router, prefix="/flow", tags=["flow"])

@app.get("/")
def read_root():
    return {"Fuck": "World"}
