from fastapi import APIRouter

from app.core.generate_edmonds_karp_visualization import generate_visualization
from app.models.graph import Graph
from app.models.visualization import Visualization

router = APIRouter()


@router.post("/generate")
def post_random_flow(graph: Graph) -> Visualization:
    """Simulate Edmonds-Karp algorithm."""
    return generate_visualization(graph)
