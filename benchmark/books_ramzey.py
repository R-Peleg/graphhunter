"""
Benchmark for Ramsey number for books.
"""
from graphhunter.invariants.books_count import CountBooks
from graphhunter.api import best_random, Goal


def benchmark_books_ramsey() -> None:
    goal = Goal(
        reward=-CountBooks(5, 7)
    )
    best_graph, best_num_books = best_random(
        num_vertices=17,
        goal=goal,
        n_graphs=100
    )
    print(f"Lowest number of books: {-best_num_books}")
    print(f"Graph edges: {best_graph.edges()}")


if __name__ == "__main__":
    # Example usage
    benchmark_books_ramsey()
