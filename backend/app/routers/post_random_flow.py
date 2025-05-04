from fastapi import APIRouter, HTTPException
from app.core.generate_random_flow import generate_random_flow
from app.models.picture import Picture

router = APIRouter()

@router.post("/generate")
def post_random_flow(n : int, density : float, allow_loops : bool, allow_reversed_edges : bool) -> Picture:
    if (n < 2):
        raise HTTPException(status_code=400, detail="n should be equal at least 2")
    return generate_random_flow(n, density, allow_loops, allow_reversed_edges)

