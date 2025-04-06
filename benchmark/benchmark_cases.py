from graphhunter.invariants import Girth, EdgeConnectivity
from graphhunter.invariants.books_count import CountBooks
from graphhunter.api import Goal
from .benchmark_case import BenchmarkCase

def get_girth_benchmark(num_vertices: int = 5) -> BenchmarkCase:
    """Create benchmark case for largest girth problem."""
    return BenchmarkCase(
        name="Largest girth in 2-edge-connected graphs",
        goal=Goal(
            reward=Girth(),
            condition=EdgeConnectivity() == 2,
        ),
        num_vertices=num_vertices,
        params={}
    )

def get_books_ramsey_benchmark() -> BenchmarkCase:
    """Create benchmark case for books Ramsey number."""
    return BenchmarkCase(
        name="Books Ramsey number",
        goal=Goal(
            reward=-CountBooks(5, 7)
        ),
        num_vertices=17,
        params={}
    )

AVAILABLE_BENCHMARKS = {
    "girth": get_girth_benchmark,
    "books": get_books_ramsey_benchmark,
}