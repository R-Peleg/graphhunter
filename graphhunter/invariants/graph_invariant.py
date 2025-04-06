from typing import Any
from abc import ABCMeta, abstractmethod
import networkx as nx


class GraphInvariant(ABCMeta):
    """
    Base class for graph invariants
    """
    @abstractmethod
    def evaluate(self, graph: nx.Graph) -> Any:
        """
        Evaluate on a specific graph
        """
        pass

    def __eq__(self, value):
        return super().__eq__(value)


class InvariantEqualToConst(GraphInvariant):
    def __init__(self, invariant: GraphInvariant, value: Any):
        self.invariant = invariant
        self.value = value
    
    def evaluate(self, graph) -> bool:
        return self.invariant.evaluate() == self.value
