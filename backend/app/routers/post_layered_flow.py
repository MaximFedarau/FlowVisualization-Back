from fastapi import APIRouter, HTTPException
from app.core.generate_layered_flow import generate_layered_flow
from app.models.picture import Picture

router = APIRouter()

@router.post("/generate")
def post_layered_flow(n : int, l : int, density : float) -> Picture:
    if (n < 2):
        raise HTTPException(status_code=400, detail="n should be equal at least 2")
    if (l < 2):
        raise HTTPException(status_code=400, detail="l should be equal at least 2")
    if (n > 2 and l == 2):
        raise HTTPException(status_code=400, detail="if n is bigger than 2, l should be equal at least 3")
    if (l > n):
        raise HTTPException(status_code=400, detail="l should not exceed n")
    return generate_layered_flow(n, l, density)

