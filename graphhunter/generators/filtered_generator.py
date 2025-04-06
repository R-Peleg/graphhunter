from graphhunter import invariants as ghi


class FilteredGenerator:
    def __init__(self, generator, filter: ghi.Invariant, trials: int):
        self.generator = generator
        self.filter = filter
        self.trials = trials
    
    def generate(self):
        for _ in range(self.trials):
            graph = self.generator.generate()
            if self.filter(graph):
                return graph
        raise ValueError(f'Could not generate a valid graph after {self.trials} trials')
