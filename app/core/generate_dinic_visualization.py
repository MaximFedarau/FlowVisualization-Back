from collections import deque

from app.constants.flow_constants import MAX_CAPACITY
from app.models.graph import Edge, Graph
from app.models.visualization import Action, Visualization


def bfs(
    edges: list[list[Edge]],
    is_visited: list[bool],
    level: list[int],
    n: int,
) -> bool:
    """Dinic's BFS."""
    queue: deque[tuple[int, int]] = deque()
    queue.append((0, 0))
    while queue:
        depth, v = queue.popleft()
        if is_visited[v]:
            continue
        is_visited[v] = True
        level[v] = depth
        for e in edges[v]:
            if e.from_ == v and ((e.capacity - e.flow) > 0):
                if not is_visited[e.to]:
                    queue.append((depth + 1, e.to))
            elif e.flow > 0 and not is_visited[e.from_]:
                queue.append((depth + 1, e.from_))
    return level[n - 1] != -1


def dfs(  # noqa: PLR0913
    way: list[Edge],
    edges: list[list[Edge]],
    level: list[int],
    ptrs: list[int],
    n: int,
    v: int,
    f: int,
) -> int:
    """Dinic's DFS."""
    if v == n - 1:
        return f
    while ptrs[v] != len(edges[v]):
        e = edges[v][ptrs[v]]
        if e.from_ == v:
            if (e.capacity == e.flow) or (level[e.to] <= level[e.from_]):
                ptrs[v] += 1
                continue
            way.append(e)
            d = dfs(way, edges, level, ptrs, n, e.to, min(f, e.capacity - e.flow))
            if d == 0:
                ptrs[v] += 1
                way.pop()
                continue
            e.flow += d
            return d
        if (e.flow == 0) or (level[e.from_] <= level[e.to]):
            ptrs[v] += 1
            continue
        way.append(e)
        d = dfs(way, edges, level, ptrs, n, e.from_, min(f, e.flow))
        if d == 0:
            ptrs[v] += 1
            way.pop()
            continue
        e.flow -= d
        return d
    return 0


def dinic(n: int, edges: list[list[Edge]]) -> Visualization:
    """Dinic's algorithm."""
    is_visited = [False for _ in range(n)]
    ptrs = [0 for _ in range(n)]
    level = [-1 for _ in range(n)]
    visualization = []
    way: list[Edge] = []
    res = 0
    while bfs(edges, is_visited, level, n):
        while True:
            way.clear()
            flow = dfs(way, edges, level, ptrs, n, 0, MAX_CAPACITY)
            if flow == 0:
                break
            res += flow
            visualization.append(Action(way=list(way), flow=flow))
        for i in range(n):
            is_visited[i] = False
            level[i] = -1
            ptrs[i] = 0
    return Visualization(visualization=visualization, flow=res)


def generate_visualization(graph: Graph) -> Visualization:
    """Generate visualization."""
    edges: list[list[Edge]] = [[] for _ in range(graph.n)]
    for edge in graph.edges:
        edges[edge.from_].append(edge)
        edges[edge.to].append(edge)
    return dinic(graph.n, edges)
