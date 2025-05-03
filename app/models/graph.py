from pydantic import BaseModel


class Edge(BaseModel):
    """Edge class."""

    from_: int
    to: int
    capacity: int
    color: tuple[int, int, int]


class Graph(BaseModel):
    """Graph class."""

    n: int
    m: int
    edges: list[Edge]
