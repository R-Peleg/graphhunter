from dataclasses import dataclass
from graphhunter.invariants import Invariant


@dataclass
class Goal:
    """
    An optimzation goal, in the form of 'maximize Reward subject to Constraint'
    """
    # A scalar reward we need to maximize
    reward: Invariant
    # A condition that must be satisfied
    condition: Invariant
