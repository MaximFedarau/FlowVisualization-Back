from app.models.graph import Graph, Edge
from app.models.visualization import Action, Visualization
from typing import List
from collections import deque

max_capacity = 100
way = []

def FindWay(n, is_visited, edges, parents):
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

def PushWay(v, f, parents):
  if (v == 0):
    return f
  e, b = parents[v]
  if (b):
      d = PushWay(e.from_, min(e.capacity - e.flow, f), parents)
      way.append(e)
      e.flow += d
      return d
  d = PushWay(e.to, min(e.flow, f), parents)
  way.append(e)
  e.flow -= d
  return d

def EdmondsKarp(n, edges):
    is_visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    visualization = []
    res = 0
    global way
    while(FindWay(n, is_visited, edges, parents)):
        way.clear()
        flow = PushWay(n - 1, max_capacity, parents)
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