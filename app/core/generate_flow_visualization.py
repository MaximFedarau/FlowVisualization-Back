from app.models.graph import Edge, Graph
from app.models.visualization import Action, Visualization

max_capacity = 1e5

way = []


def dfs(
    edges: list[list[Edge]],
    is_visited: list[bool],
    n: int,
    v: int,
    f: float,
) -> int:
    """Ford Fulkerson Dfs."""
    is_visited[v] = True
    if v == n - 1:
        return f  # type: ignore[return-value]
    for edge in edges[v]:
        if edge.from_ == v:
            if is_visited[edge.to] or (edge.capacity - edge.flow == 0):
                continue
            way.append(edge)
            res = dfs(edges, is_visited, n, edge.to, min(f, edge.capacity - edge.flow))
            if res > 0:
                edge.flow += res
                return res
            way.pop()
        else:
            if is_visited[edge.from_] or edge.flow == 0:
                continue
            way.append(edge)
            res = dfs(edges, is_visited, n, edge.from_, min(f, edge.flow))
            if res > 0:
                edge.flow -= res
                return res
            way.pop()
    return 0


def ford_fulkerson(n: int, edges: list[list[Edge]]) -> Visualization:
    """Ford-Fulkerson algorithm."""
    is_visited = [False for _ in range(n)]
    visualization: list[Action] = []
    res = 0
    while True:
        global way  # noqa: PLW0602
        way.clear()
        for i in range(n):
            is_visited[i] = False
        flow = dfs(edges, is_visited, n, 0, max_capacity)
        if flow == 0:
            return Visualization(visualization=visualization, flow=res)
        res += flow
        visualization.append(Action(way=list(way), flow=flow))


def generate_flow_visualization(graph: Graph) -> Visualization:
    """Generate flow visualization."""
    edges: list[list[Edge]] = [[] for _ in range(graph.n)]
    for edge in graph.edges:
        edges[edge.from_].append(edge)
        edges[edge.to].append(edge)
    return ford_fulkerson(graph.n, edges)
