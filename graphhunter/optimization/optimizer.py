from typing import Tuple
import networkx as nx
from abc import ABCMeta, abstractmethod


class Optimizer(metaclass=ABCMeta):
    @abstractmethod
    def find_max(invariant) -> Tuple[nx.Graph, float]:
        """
        Find maximal value for a scalar invariant
        """
