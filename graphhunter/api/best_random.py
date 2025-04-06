from graphhunter.generators import ErdosRenyiGenerator, FilteredGenerator
from graphhunter.optimization import BestOfN
from .goal import Goal


def best_random(goal: Goal, num_vertices: int, n_graphs: int):
    """
    Find a graph towards a goal by choosing the best one among n random graphs
    """
    generator = ErdosRenyiGenerator(num_vertices, 0.5)
    if goal.condition is not None:
        generator = FilteredGenerator(generator, goal.condition, 1000)
    optimizer = BestOfN(generator, n_graphs)
    return optimizer.find_max(goal.reward)
