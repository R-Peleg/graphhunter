"""
Benchmark Runner for GraphHunter
This script runs various benchmark cases using the GraphHunter library.

Usage: `python -m benchmark.benchmark_runner [--benchmark BENCHMARK_NAME] [--n-graphs N]`
"""
import argparse
from typing import Callable
from graphhunter.api import best_random, Goal
from benchmark.benchmark_case import BenchmarkCase
from benchmark.benchmark_cases import AVAILABLE_BENCHMARKS

def run_random_search(benchmark: BenchmarkCase, n_graphs: int = 100) -> tuple:
    """Run random search for given benchmark case."""
    print(f"\nRunning {benchmark}")
    best_graph, best_value = best_random(
        num_vertices=benchmark.num_vertices,
        goal=benchmark.goal,
        n_graphs=n_graphs
    )
    return best_graph, best_value

def print_results(benchmark: BenchmarkCase, best_graph, best_value, runtime):
    """Print benchmark results."""
    print(f"Run time: {runtime}")
    print(f"Best value: {best_value}")
    print(f"Graph edges: {best_graph.edges()}")

def run_benchmark_case(case: BenchmarkCase, 
                 search_method: Callable = run_random_search,
                 **search_params):
    """Run the benchmark with specified search method."""
    start_time = time.time()
    best_graph, best_value = search_method(benchmark, **search_params)
    end_time = time.time()
    print_results(benchmark, best_graph, best_value, end_time - start_time)

def parse_arguments():
    parser = argparse.ArgumentParser(description='GraphHunter Benchmark Runner')
    parser.add_argument(
        '--benchmark',
        type=str,
        choices=list(AVAILABLE_BENCHMARKS.keys()),
        default=list(AVAILABLE_BENCHMARKS.keys())[0],
        help='Benchmark case to run'
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    # Run selected benchmark
    benchmark = AVAILABLE_BENCHMARKS[args.benchmark]()
    for case in benchmark:
        run_benchmark_case(case, n_graphs=1000)
