from pydantic import BaseModel, Field
from typing import List, Tuple
from app.models.graph import Graph

class Picture(BaseModel):
    graph: Graph
    coordinates: List[Tuple[float, float]]
