import networkx as nx
from graphhunter.invariants.girth import Girth
from graphhunter.generators.erdos_reyni import ErdosRenyiGenerator
from graphhunter.optimization.best_of_n import BestOfN

def is_2_edge_connected(graph):
    """Check if a graph is 2-edge-connected."""
    return nx.edge_connectivity(graph) >= 2

def benchmark_largest_girth(num_vertices, num_trials):
    """Find the graph with the largest girth among 2-edge-connected graphs."""
    generator = ErdosRenyiGenerator(num_vertices, 0.5)
    girth_invariant = Girth()
    optimizer = BestOfN(generator, num_trials)

    # Generate and optimize
    best_graph, best_girth = optimizer.find_max(girth_invariant)
    print(f"Largest girth: {best_girth}")
    print(f"Graph edges: {best_graph.edges()}")


if __name__ == "__main__":
    benchmark_largest_girth(num_vertices=5, num_trials=100)
