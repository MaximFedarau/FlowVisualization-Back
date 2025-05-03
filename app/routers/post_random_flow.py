from fastapi import APIRouter, HTTPException

from app.constants.random_flow import MIN_EDGES_QUANTITY
from app.core.generate_random_flow import generate_random_flow
from app.models.picture import Picture

router = APIRouter()


@router.post("/generate")
def post_random_flow(n: int, m: int) -> Picture:
    """Generate random flow handler."""
    if n < MIN_EDGES_QUANTITY:
        raise HTTPException(status_code=400, detail="n should be equal at least 2")
    return generate_random_flow(n, m)
