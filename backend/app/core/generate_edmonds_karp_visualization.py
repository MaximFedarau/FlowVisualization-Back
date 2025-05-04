from app.models.graph import Graph, Edge
from app.models.visualization import Action, Visualization
from collections import deque
from app.constants.flow_constants import max_capacity

def FindWay(n : int, is_visited : list[bool], edges : list[list[Edge]], parents : list[tuple[Edge, bool]]) -> bool:
    queue = deque()
    queue.append(0)
    while (queue):
        v = queue.popleft()
        if is_visited[v]:
          continue
        is_visited[v] = True
        for e in edges[v]:
            if (e.from_ == v and (e.capacity - e.flow > 0) and not is_visited[e.to]):
                parents[e.to] = (e, True)
                queue.append(e.to)
            elif (e.flow > 0 and not is_visited[e.from_]):
                parents[e.from_] = (e, False)
                queue.append(e.from_)
    return is_visited[n - 1]

def PushWay(v : int, f : int, parents : list[tuple[Edge]], way) -> int:
  if (v == 0):
    return f
  e, b = parents[v]
  if (b):
      d = PushWay(e.from_, min(e.capacity - e.flow, f), parents, way)
      way.append(e)
      e.flow += d
      return d
  d = PushWay(e.to, min(e.flow, f), parents, way)
  way.append(e)
  e.flow -= d
  return d

def EdmondsKarp(n : int, edges : list[list[Edge]]) -> Visualization:
    is_visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    visualization = []
    way = []
    res = 0
    while(FindWay(n, is_visited, edges, parents)):
        way.clear()
        flow = PushWay(n - 1, max_capacity, parents, way)
        res += flow
        visualization.append(Action(way=list(way), flow=flow))
        for i in range(n):
            parents[i] = None
            is_visited[i] = False
    return Visualization(visualization=visualization, flow=res)

def generate_visualization(graph : Graph) -> Visualization:
    edges = [[] for _ in range(graph.n)]
    for edge in graph.edges:
        edges[edge.from_].append(edge)
        edges[edge.to].append(edge)
    return EdmondsKarp(graph.n, edges)