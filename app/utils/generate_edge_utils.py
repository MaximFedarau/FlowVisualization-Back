import random

from app.constants.flow_constants import max_capacity, min_capacity
from app.models.graph import Edge


def add_edge(u: int, v: int, edges: list[Edge]) -> None:
    """Add edge."""
    r = random.randint(0, 255)  # noqa: S311
    g = random.randint(0, 255)  # noqa: S311
    b = random.randint(0, 255)  # noqa: S311
    edge = Edge(
        from_=u,
        to=v,
        capacity=random.randint(min_capacity, max_capacity),  # noqa: S311
        flow=0,
        color=(r, g, b),
    )
    edges.append(edge)
