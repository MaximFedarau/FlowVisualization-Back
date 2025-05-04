import random

from app.models.graph import Edge, Graph
from app.models.picture import Picture
from app.utils.generate_flow_utils import add_edge

def get_coordinates(coordinates : list[float], layeres_counts : list[int], left_border : float, right_border : float, up_border : float, down_border : float, l : int) -> None:
    for i in range(l):
        x = (right_border * i + left_border * (l - 1 - i)) / (l - 1)
        for j in range(1, layeres_counts[i] + 1):
            y = (j * down_border + (layeres_counts[i] + 1 - j) * up_border) / (layeres_counts[i] + 1)
            coordinates.append((x, y))

def generate_layered_flow(n : int, l : int, density: float) -> Picture:
    edges = []
    coordinates = []
    layeres_counts = [1 for _ in range(l)]
    distribution = [random.randint(1, l - 2) for _ in range(n - l)]
    for level in distribution:
        layeres_counts[level] += 1
    layeres = [[] for _ in range(l)]
    count = 0
    for i in range(l):
        for number in range(layeres_counts[i]):
            layeres[i].append(count)
            count += 1
    left_border = -10
    right_border = 10
    up_border = 10
    down_border = -10
    for i in range(l - 1):
        for u in layeres[i]:
            for v in layeres[i + 1]:
                if (random.random() < density):
                    add_edge(u, v, edges)
    get_coordinates(coordinates, layeres_counts, left_border, right_border, up_border, down_border, l)
    graph = Graph(n=n, m=len(edges), edges=edges)
    picture = Picture(graph=graph, coordinates=coordinates)
    return picture