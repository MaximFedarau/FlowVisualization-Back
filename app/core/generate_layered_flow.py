import random

from app.models.graph import Edge, Graph
from app.models.picture import Picture
from app.utils.generate_edge_utils import add_edge


def get_coordinates(  # noqa: PLR0913
    coordinates: list[tuple[float, float]],
    layeres_counts: list[int],
    left_border: float,
    right_border: float,
    up_border: float,
    down_border: float,
    layers: int,
) -> None:
    """Get coordinates."""
    for i in range(layers):
        x = (right_border * i + left_border * (layers - 1 - i)) / (layers - 1)
        for j in range(1, layeres_counts[i] + 1):
            y = (j * down_border + (layeres_counts[i] + 1 - j) * up_border) / (
                layeres_counts[i] + 1
            )
            coordinates.append((x, y))


def generate_layered_flow(
    n: int,
    requested_layers_quantity: int,
    density: float,
) -> Picture:
    """Generate layered flow."""
    edges: list[Edge] = []
    coordinates: list[tuple[float, float]] = []
    layeres_counts = [1 for _ in range(requested_layers_quantity)]
    distribution = [
        random.randint(1, requested_layers_quantity - 2)  # noqa: S311
        for _ in range(n - requested_layers_quantity)
    ]
    for level in distribution:
        layeres_counts[level] += 1
    layeres: list[list[int]] = [[] for _ in range(requested_layers_quantity)]
    count = 0
    for i in range(requested_layers_quantity):
        for _ in range(layeres_counts[i]):
            layeres[i].append(count)
            count += 1
    left_border = -10
    right_border = 10
    up_border = 10
    down_border = -10
    for i in range(requested_layers_quantity - 1):
        for u in layeres[i]:
            for v in layeres[i + 1]:
                if random.random() < density:  # noqa: S311
                    add_edge(u, v, edges)
    get_coordinates(
        coordinates,
        layeres_counts,
        left_border,
        right_border,
        up_border,
        down_border,
        requested_layers_quantity,
    )
    graph = Graph(n=n, m=len(edges), edges=edges)
    return Picture(graph=graph, coordinates=coordinates)
