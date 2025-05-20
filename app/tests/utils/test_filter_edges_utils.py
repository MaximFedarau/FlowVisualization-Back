from app.models.graph import Edge
from app.utils.filter_edges_utils import (
    filter_loops,
    filter_multiple_edges,
    filter_reversed_edges,
)


def test_filter_loops() -> None:
    """Test filter_loops."""
    edge1 = Edge(from_=0, to=0, capacity=2, flow=0, color=(0, 0, 0))
    edge2 = Edge(from_=0, to=2, capacity=2, flow=0, color=(0, 0, 0))
    edges = [edge1, edge2]
    filtered_edges = filter_loops(edges)
    assert len(filtered_edges) == 1
    assert edge1 not in filtered_edges
    assert edge2 in filtered_edges


def test_filter_reversed_edges() -> None:
    """Test filter_reversed_edges."""
    edge1 = Edge(from_=0, to=1, capacity=2, flow=0, color=(0, 0, 0))
    edge2 = Edge(from_=1, to=0, capacity=2, flow=0, color=(0, 0, 0))
    edges = [edge1, edge2]
    filtered_edges = filter_reversed_edges(edges)
    assert len(filtered_edges) == 1


def test_filter_multiple_edges() -> None:
    """Test filter_multiple_edges."""
    edge1 = Edge(from_=0, to=1, capacity=2, flow=0, color=(0, 0, 0))
    edge2 = Edge(from_=0, to=1, capacity=2, flow=0, color=(0, 0, 0))
    edges = [edge1, edge2]
    filtered_edges = filter_multiple_edges(edges)
    assert len(filtered_edges) == 1
