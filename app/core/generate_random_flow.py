import math
import random

from app.models.graph import Edge, Graph
from app.models.picture import Picture
from app.utils.filter_edges_utils import filter_loops, filter_reversed_edges
from app.utils.generate_edge_utils import add_edge


def get_point_on_circle(
    centre_x: float,
    centre_y: float,
    radius: float,
    angle: float,
) -> tuple[float, float]:
    """Get point on circle."""
    x = centre_x + radius * math.cos(angle)
    y = centre_y + radius * math.sin(angle)
    return (x, y)


def generate_random_flow(
    n: int,
    density: float,
    allow_loops: bool,  # noqa: FBT001
    allow_reversed_edges: bool,  # noqa: FBT001
) -> Picture:
    """Generate random flow."""
    edges: list[Edge] = []
    coordinates = []
    for i in range(n):
        for j in range(n):
            if random.random() < density:  # noqa: S311
                add_edge(i, j, edges)
    if not allow_loops:
        edges = filter_loops(edges)
    if not allow_reversed_edges:
        edges = filter_reversed_edges(edges)

    graph = Graph(n=n, m=len(edges), edges=edges)
    centre_x = 0
    centre_y = 0
    radius = 10
    for i in range(n):
        angle = 2 * math.pi * i / n
        p = get_point_on_circle(centre_x, centre_y, radius, angle)
        coordinates.append(p)
    return Picture(graph=graph, coordinates=coordinates)
