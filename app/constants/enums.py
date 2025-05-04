from app.core.generate_dinic_visualization import generate_visualization as generate_dinic
from app.core.generate_edmonds_karp_visualization import (
    generate_visualization as generate_edmonds_karp,
)
from app.core.generate_ford_fullkerson_visualization import (
    generate_visualization as generate_ford_fukerson,
)

AlgorithmEnum = {
    "ford_fulkerson": generate_ford_fukerson,
    "edmonds_karp": generate_edmonds_karp,
    "dinic": generate_dinic,
}
