"""
Benchmark Runner for GraphHunter
This script runs various benchmark cases using the GraphHunter library.

Usage: `python -m benchmark.benchmark_runner`
"""
from typing import Callable
from graphhunter.api import best_random, Goal
from benchmark.benchmark_case import BenchmarkCase

def run_random_search(benchmark: BenchmarkCase, n_graphs: int = 100) -> tuple:
    """Run random search for given benchmark case."""
    print(f"\nRunning {benchmark}")
    best_graph, best_value = best_random(
        num_vertices=benchmark.num_vertices,
        goal=benchmark.goal,
        n_graphs=n_graphs
    )
    return best_graph, best_value

def print_results(benchmark: BenchmarkCase, best_graph, best_value):
    """Print benchmark results."""
    print(f"Best value: {best_value}")
    print(f"Graph edges: {best_graph.edges()}")

def run_benchmark(benchmark: BenchmarkCase, 
                 search_method: Callable = run_random_search,
                 **search_params):
    """Run the benchmark with specified search method."""
    best_graph, best_value = search_method(benchmark, **search_params)
    print_results(benchmark, best_graph, best_value)

if __name__ == "__main__":
    from benchmark.benchmark_cases import AVAILABLE_BENCHMARKS
    
    # Run all available benchmarks
    for name, get_benchmark in AVAILABLE_BENCHMARKS.items():
        benchmark = get_benchmark()
        run_benchmark(benchmark, n_graphs=100)
