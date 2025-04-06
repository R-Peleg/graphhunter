from dataclasses import dataclass
from graphhunter.invariants import GraphInvariant


@dataclass
class Goal:
    """
    An optimzation goal, in the form of 'maximize Reward subject to Constraint'
    """
    # A scalar reward we need to maximize
    reward: GraphInvariant
    # A condition that must be satisfied
    condition: GraphInvariant
