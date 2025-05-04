from fastapi import APIRouter, HTTPException

from app.constants.flow_constants import MIN_EDGES_QUANTITY
from app.core.generate_random_flow import generate_random_flow
from app.models.picture import Picture

router = APIRouter()


@router.post("/generate")
def post_random_flow(
    n: int,
    density: float,
    allow_loops: bool,  # noqa: FBT001
    allow_reversed_edges: bool,  # noqa: FBT001
) -> Picture:
    """Generate random flow handler."""
    if n < MIN_EDGES_QUANTITY:
        raise HTTPException(status_code=400, detail="n should be equal at least 2")
    return generate_random_flow(n, density, allow_loops, allow_reversed_edges)
