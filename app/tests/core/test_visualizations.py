from copy import deepcopy
from typing import TYPE_CHECKING

from app.core.generate_dinic_visualization import (
    generate_visualization as dinic_visualization,
)
from app.core.generate_edmonds_karp_visualization import (
    generate_visualization as endmonds_karp_visualization,
)
from app.core.generate_ford_fullkerson_visualization import (
    generate_visualization as ford_fulkerson_visualization,
)
from app.core.generate_random_flow import generate_random_flow

if TYPE_CHECKING:
    from app.models.picture import Picture


def test_algorithms() -> None:
    """Test algorithms correctess."""
    graph: Picture = generate_random_flow(50, 0.5, True, True)  # noqa: FBT003
    ford_fulkerson_value = ford_fulkerson_visualization(deepcopy(graph).graph).flow
    dinic_value = dinic_visualization(deepcopy(graph).graph).flow
    edmonds_karp_value = endmonds_karp_visualization(deepcopy(graph).graph).flow
    assert ford_fulkerson_value == dinic_value
    assert edmonds_karp_value == dinic_value
