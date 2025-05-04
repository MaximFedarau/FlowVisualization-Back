from fastapi import APIRouter

from app.core.generate_flow_visualization import generate_flow_visualization
from app.models.graph import Graph
from app.models.visualization import Visualization

router = APIRouter()


@router.post("/generate")
def post_random_flow(graph: Graph) -> Visualization:
    """Generate random flow."""
    return generate_flow_visualization(graph)
