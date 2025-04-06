import networkx as nx
from graphhunter.invariants import Girth, EdgeConnectivity
from graphhunter.api import best_random, Goal

def benchmark_largest_girth(num_vertices, num_trials):
    """Find the graph with the largest girth among 2-edge-connected graphs."""
    goal = Goal(
        reward=Girth(),
        condition=EdgeConnectivity() == 2,
    )
    best_graph, best_girth = best_random(
        num_vertices=num_vertices,
        goal=goal,
        n_graphs=100
    )
    print(f"Largest girth: {best_girth}")
    print(f"Graph edges: {best_graph.edges()}")


if __name__ == "__main__":
    benchmark_largest_girth(num_vertices=5, num_trials=100)
