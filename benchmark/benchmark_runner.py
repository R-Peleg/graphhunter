from test_girth_benchmark_case import benchmark_largest_girth

def run_benchmark():
    """Run the benchmark cases."""
    print("Running benchmark for largest girth in 2-edge-connected graphs...")
    benchmark_largest_girth(num_vertices=5, num_trials=100)

if __name__ == "__main__":
    run_benchmark()
