from fastapi import APIRouter, HTTPException
from app.core.generate_edmonds_karp_visualization import generate_visualization
from app.models.graph import Graph
from app.models.visualization import Visualization
from typing import List

router = APIRouter()

@router.post("/generate")
def post_random_flow(graph : Graph) -> Visualization:
    visualization = generate_visualization(graph)
    return visualization