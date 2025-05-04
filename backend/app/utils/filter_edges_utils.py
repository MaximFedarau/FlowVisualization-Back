from app.models.graph import Edge

def filter_multiple_edges(edges: list[Edge]) -> list[Edge]:
    used = set()
    clear_edges = []
    for edge in edges:
        if ((edge.from_, edge.to) not in used):
            used.add((edge.from_, edge.to))
            clear_edges.append(edge)
    return clear_edges

def filter_reversed_edges(edges: list[Edge]) -> list[Edge]:
    used = set()
    clear_edges = []
    for edge in edges:
        if ((edge.to, edge.from_) not in used):
            used.add((edge.from_, edge.to))
            clear_edges.append(edge)
    return clear_edges

def filter_loops(edges : list[Edge]) -> list[Edge]:
    clear_edges = []
    for edge in edges:
        if (edge.to != edge.from_):
            clear_edges.append(edge)
    return clear_edges