from pydantic import BaseModel, Field
from typing import List,Tuple

class Edge(BaseModel):
    from_: int
    to: int
    capacity: int
    flow : int
    color: Tuple[int, int, int]

class Graph(BaseModel):
    n: int
    m: int
    edges: List[Edge]
