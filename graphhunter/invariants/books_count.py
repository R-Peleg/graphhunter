import networkx as nx
from . import GraphInvariant
from graphhunter.external.ramsey_books_wheels.ramsey_funcs import count_books, neighbors, common_neighbors


class CountBooks(GraphInvariant):
    """
    Count the number of books in the graph and its complement.
    Used for Ramsey numbers involving books.
    Invariant type: Non-negative integer.
    """

    def __init__(self, books_size_graph, book_size_complement):
        """
        Initialize the CountBooks class.

        Parameters:
        books_size_graph (int): The size of the graph.
        book_size_complement (int): The size of the complement of the book.
        Note: We define B_n as n-vertices book here. Some places define it as n+2-vertices book so beware.
        """
        self.books_size_graph = books_size_graph
        self.book_size_complement = book_size_complement

    def evaluate(self, graph: nx.Graph) -> int:
        adj_matrix = nx.to_numpy_array(graph).astype(int)
        num_verts = len(graph.nodes)
        neighbors_mat = neighbors(
            adj_matrix=adj_matrix,
            num_verts=num_verts,
            num_colors=2,
        )
        common_neighbors_mat = common_neighbors(
            neighbors=neighbors_mat,
            num_verts=num_verts,
            num_colors=2,
        )
        return count_books(adj_matrix, common_neighbors=common_neighbors_mat, num_verts=num_verts,
                           bad_sizes=[self.books_size_graph, self.book_size_complement])
