from pydantic import BaseModel


class Edge(BaseModel):
    from_: int
    to: int
    capacity: int
    flow: int
    color: tuple[int, int, int]


class Graph(BaseModel):
    n: int
    m: int
    edges: list[Edge]
