import math
import random

from app.constants.flow_constants import max_capacity, min_capacity
from app.models.graph import Edge, Graph
from app.models.picture import Picture


def filter_loops(edges: list[Edge]) -> list[Edge]:
    """Filter loops."""
    return [edge for edge in edges if edge.to != edge.from_]


def filter_multiple_edges(edges: list[Edge]) -> list[Edge]:
    """Filter multiple edges."""
    used = set()
    clear_edges = []
    for edge in edges:
        if (edge.from_, edge.to) not in used:
            used.add((edge.from_, edge.to))
            clear_edges.append(edge)
    return clear_edges


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


def generate_random_flow(n: int, m: int) -> Picture:
    """Generate random flow."""
    edges: list[Edge] = []
    coordinates = []
    for _ in range(m):
        u = random.randint(0, n - 1)  # noqa: S311
        v = random.randint(0, n - 1)  # noqa: S311
        add_edge(u, v, edges)

    edges = filter_loops(edges)
    edges = filter_multiple_edges(edges)

    graph = Graph(n=n, m=len(edges), edges=edges)
    centre_x = 0
    centre_y = 0
    radius = 10
    for i in range(n):
        angle = 2 * math.pi * i / n
        p = get_point_on_circle(centre_x, centre_y, radius, angle)
        coordinates.append(p)
    return Picture(graph=graph, coordinates=coordinates)
