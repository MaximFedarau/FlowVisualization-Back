from fastapi import APIRouter, HTTPException
from app.core.generate_dinic_visualization import generate_visualization
from app.models.graph import Graph
from app.models.visualization import Visualization

router = APIRouter()

@router.post("/generate")
def post_dinic(graph : Graph) -> Visualization:
    visualization = generate_visualization(graph)
    return visualization