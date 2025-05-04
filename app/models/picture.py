from typing import List, Tuple

from pydantic import BaseModel

from app.models.graph import Graph


class Picture(BaseModel):
    graph: Graph
    coordinates: List[Tuple[float, float]]
