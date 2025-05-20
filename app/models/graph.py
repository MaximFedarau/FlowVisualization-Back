from pydantic import BaseModel


class Edge(BaseModel):
    """Edge model."""

    from_: int
    to: int
    capacity: int
    flow: int
    color: tuple[int, int, int]


class Graph(BaseModel):
    """Graph model."""

    n: int
    m: int
    edges: list[Edge]
