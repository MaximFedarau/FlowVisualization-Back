import random
from app.constants.flow_constants import max_capacity, min_capacity
from app.models.graph import Edge

def add_edge(u : int, v : int, edges : list[Edge]) -> None:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    edge = Edge(
        from_=u,
        to=v,
        capacity=random.randint(min_capacity, max_capacity),
        flow=0,
        color=(r, g, b),
    )
    edges.append(edge)