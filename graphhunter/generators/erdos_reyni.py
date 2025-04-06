import networkx as nx

class ErdosRenyiGenerator:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def generate_graph(arg_dict):
        seed = arg_dict.get('seed')
        return nx.erdos_renyi_graph(self.n, self.p, seed=seed)
