from graphhunter import generators as ghg, optimization as gho


def best_random(goal: Goal, num_vertices: int, n_graphs: int):
    """
    Find a graph towards a goal by choosing the best one among n random graphs
    """
    generator = ghg.FilteredGenerator(
        ghg.ErdosRenyiGenerator(num_vertices, 0.5),
        goal.condition
    )
    optimizer = gho.BestOfNOptimizer(n_graphs)
    return optimizer.find_max(goal.reward)
