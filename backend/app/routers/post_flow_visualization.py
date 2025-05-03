from fastapi import APIRouter, HTTPException
from app.core.generate_flow_visualization import generate_flow_visualization
from app.models.graph import Graph
from app.models.visualization import Visualization
from typing import List

router = APIRouter()

@router.post("/generate")
def post_random_flow(graph : Graph) -> Visualization:
    visualization = generate_flow_visualization(graph)
    return visualization