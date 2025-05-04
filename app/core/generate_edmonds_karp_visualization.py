from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

from fastapi import HTTPException

from app.constants.flow_constants import MAX_CAPACITY

if TYPE_CHECKING:
    from app.models.graph import Edge, Graph
from app.models.visualization import Action, Visualization


def find_way(
    n: int,
    is_visited: list[bool],
    edges: list[list[Edge]],
    parents: list[None | tuple[Edge, bool]],
) -> bool:
    """Find way."""
    queue: deque[int] = deque()
    queue.append(0)
    while queue:
        v = queue.popleft()
        if is_visited[v]:
            continue
        is_visited[v] = True
        for e in edges[v]:
            if e.from_ == v and (e.capacity - e.flow > 0) and not is_visited[e.to]:
                parents[e.to] = (e, True)
                queue.append(e.to)
            elif e.flow > 0 and not is_visited[e.from_]:
                parents[e.from_] = (e, False)
                queue.append(e.from_)
    return is_visited[n - 1]


def push_way(
    v: int,
    f: float,
    parents: list[None | tuple[Edge, bool]],
    way: list[Edge],
) -> int:
    """Push way."""
    if v == 0:
        return f  # type: ignore [return-value]
    parent = parents[v]
    if parent is None:
        raise HTTPException(
            status_code=404,
            detail="Edmondsk Karp failed.",
        )
    e, b = parent
    if b:
        d = push_way(e.from_, min(e.capacity - e.flow, f), parents, way)
        way.append(e)
        e.flow += d
        return d
    d = push_way(e.to, min(e.flow, f), parents, way)
    way.append(e)
    e.flow -= d
    return d


def edmonds_karp(n: int, edges: list[list[Edge]]) -> Visualization:
    """Edmonds-Karp algorithm."""
    is_visited = [False for _ in range(n)]
    parents: list[None | tuple[Edge, bool]] = [None for _ in range(n)]
    visualization = []
    way: list[Edge] = []
    res = 0
    while find_way(n, is_visited, edges, parents):
        way.clear()
        flow = push_way(n - 1, MAX_CAPACITY, parents, way)
        res += flow
        visualization.append(Action(way=list(way), flow=flow))
        for i in range(n):
            parents[i] = None
            is_visited[i] = False
    return Visualization(visualization=visualization, flow=res)


def generate_visualization(graph: Graph) -> Visualization:
    """Generate visualization."""
    edges: list[list[Edge]] = [[] for _ in range(graph.n)]
    for edge in graph.edges:
        edges[edge.from_].append(edge)
        edges[edge.to].append(edge)
    return edmonds_karp(graph.n, edges)
