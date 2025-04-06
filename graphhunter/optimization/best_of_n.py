from graphhunter.optimization import Optimizer


class BestOfN(Optimizer):
    """
    Select the best result out of n trials
    """
    def __init__(generator, n):
        self.generator = generator
        self.n = n

    def find_max(invariant):
        best = None
        best_score = float('-inf')
        for _ in range(n):
            graph = self.generator.generate()
            score = invariant.evaluate(graph)
            if score > best_score:
                best = graph
                best_score = score
        return best, best_score
