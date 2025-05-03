import random
import math

from app.models.graph import Edge
from app.models.graph import Graph
from app.models.picture import Picture
from typing import List, Tuple

def filter_loops(edges : List[Edge]) -> List[Edge]:
    clear_edges = []
    for edge in edges:
        if (edge.to != edge.from_):
            clear_edges.append(edge)
    return clear_edges

def filter_multiple_edges(edges: List[Edge]) -> List[Edge]:
    used = set()
    clear_edges = []
    for edge in edges:
        if ((edge.from_, edge.to) not in used):
            used.add((edge.from_, edge.to))
            clear_edges.append(edge)
    return clear_edges

def get_point_on_circle(centre_x : float, centre_y : float, radius : float, angle : float) -> Tuple[float, float]:
    x = centre_x + radius * math.cos(angle)
    y = centre_y + radius * math.sin(angle)
    return (x, y)

def add_edge(u : int, v : int, edges : List[Edge]) -> None:
    min_cap = 1
    max_cap = 100
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    edge = Edge(
        from_=u,
        to=v,
        capacity=random.randint(min_cap, max_cap),
        flow=0,
        color=(r, g, b),
    )
    edges.append(edge)
def generate_random_flow(n : int, m : int) -> Picture:
    print("DEBUG: generate_random_flow called with n =", n, "m =", m)
    edges = []
    coordinates = []
    for i in range(m):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
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
    picture = Picture(graph=graph, coordinates=coordinates)
    return picture