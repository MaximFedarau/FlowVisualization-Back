from fastapi import APIRouter, HTTPException

from app.constants.flow_constants import MIN_EDGES_QUANTITY
from app.core.generate_layered_flow import generate_layered_flow
from app.models.picture import Picture

router = APIRouter()


@router.post("/generate")
def post_layered_flow(n: int, layers: int, density: float) -> Picture:
    """Post layered flow."""
    if n < MIN_EDGES_QUANTITY:
        raise HTTPException(status_code=400, detail="n should be equal at least 2")
    if layers < MIN_EDGES_QUANTITY:
        raise HTTPException(status_code=400, detail="l should be equal at least 2")
    if n > MIN_EDGES_QUANTITY and layers == MIN_EDGES_QUANTITY:
        raise HTTPException(
            status_code=400,
            detail="if n is bigger than 2, l should be equal at least 3",
        )
    if layers > n:
        raise HTTPException(status_code=400, detail="l should not exceed n")
    return generate_layered_flow(n, layers, density)
