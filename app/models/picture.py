from pydantic import BaseModel

from app.models.graph import Graph


class Picture(BaseModel):
    """Picture class."""

    graph: Graph
    coordinates: list[tuple[float, float]]
