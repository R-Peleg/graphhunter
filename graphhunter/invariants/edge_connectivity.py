import networkx as nx
from graphhunter.invariants import GraphInvariant


class EdgeConnectivity(GraphInvariant):
    """
    The Edge Connectivity of the graph
    """
    def evaluate(self, graph: nx.Graph) -> Any:
        """
        Evaluate on a specific graph
        """
        return nx.edge_connectivity(G)
