from pydantic import BaseModel

from app.models.graph import Graph


class Picture(BaseModel):
    """Picture model."""

    graph: Graph
    coordinates: list[tuple[float, float]]
