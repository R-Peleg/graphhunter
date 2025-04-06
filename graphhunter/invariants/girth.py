import networkx as nx
from graphhunter.invariants import GraphInvariant


class Girth(GraphInvariant):
    """
    The Girth, length of the minimal cycle, of a graph
    """
    def evaluate(self, graph: nx.Graph) -> Any:
        """
        Evaluate on a specific graph
        """
        cycles = nx.minimum_cycle_basis(G)
        return min(len(cycle) for cycle in cycles)
