from typing import TYPE_CHECKING

from app.constants.flow_constants import MAX_CAPACITY, MIN_CAPACITY

if TYPE_CHECKING:
    from app.models.graph import Edge
from app.utils.generate_edge_utils import add_edge


def test_add_edge() -> None:
    """Test add_edge method."""
    edges: list[Edge] = []
    from_node = 0
    to_node = 1
    add_edge(from_node, to_node, edges)
    assert len(edges) == 1
    assert edges[0].from_ == from_node
    assert edges[0].to == to_node
    assert edges[0].capacity >= MIN_CAPACITY
    assert edges[0].capacity <= MAX_CAPACITY
