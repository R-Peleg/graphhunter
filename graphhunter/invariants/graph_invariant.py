from typing import Any
from abc import ABCMeta, abstractmethod
import networkx as nx


class GraphInvariant(metaclass=ABCMeta):
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
        if isinstance(value, (float, int)):
            return InvariantEqualToConst(self, value)
        elif isinstance(value, GraphInvariant):
            raise NotImplementedError("Equality comparison between two invariants is not implemented.")
        else:
            raise TypeError(f"Unsupported type for equality comparison: {type(value)}")


class InvariantEqualToConst(GraphInvariant):
    def __init__(self, invariant: GraphInvariant, value: Any):
        self.invariant = invariant
        self.value = value
    
    def evaluate(self, graph) -> bool:
        return self.invariant.evaluate(graph) == self.value
