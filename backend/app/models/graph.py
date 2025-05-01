from pydantic import BaseModel, Field
from typing import List

class Edge(BaseModel):
    from_: int = Field(...)
    to: int = Field(...)
    capacity: int = Field(0, ge=0)
    flow: int = Field(0, ge=0)
    color: int = Field(0)

class Graph(BaseModel):
    n: int
    m: int
    edges: List[List[Edge]]
