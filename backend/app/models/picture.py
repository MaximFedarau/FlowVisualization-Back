from pydantic import BaseModel, Field
from app.models.graph import Graph

class Picture(BaseModel):
    graph: Graph
    coordinates: list[tuple[float, float]]
