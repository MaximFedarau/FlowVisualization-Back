from fastapi import APIRouter, HTTPException
from app.core.generate_random_flow import generate_random_flow
from app.models.picture import Picture

router = APIRouter()

@router.post("/generate")
def post_random_flow(n : int, m : int) -> Picture:
    if (n < 2):
        raise HTTPException(status_code=400, detail="n should be equal at least 2")
    return generate_random_flow(n, m)

