from graphhunter.invariants import GraphInvariant


class FilteredGenerator:
    def __init__(self, generator, filter: GraphInvariant, trials: int):
        self.generator = generator
        self.filter = filter
        self.trials = trials
    
    def generate_graph(self, arg_dict=None):
        for _ in range(self.trials):
            graph = self.generator.generate_graph(arg_dict)
            if self.filter.evaluate(graph):
                return graph
        raise ValueError(f'Could not generate a valid graph after {self.trials} trials')
