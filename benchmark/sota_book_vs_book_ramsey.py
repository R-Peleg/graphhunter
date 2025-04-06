"""
Benchmark to include State Of The Art lower bounds for Book vs. Book Ramsye numbers.
"""
from graphhunter.invariants.books_count import CountBooks
from graphhunter.api import Goal
from .benchmark_case import BenchmarkCase


def sota_book_vs_book_goals():
    # Data from https://www.combinatorics.org/files/Surveys/ds1/ds1v16-2021.pdf, table IXa.
    return [
        BenchmarkCase(
            name="R(B3, B3)",
            goal=Goal(
                reward=-CountBooks(3, 3)
            ),
            goal_target=0,
            num_vertices=6,
            params={}
        ),
        BenchmarkCase(
            name="R(B3, B4)",
            goal=Goal(
                reward=-CountBooks(3, 4)
            ),
            goal_target=0,
            num_vertices=7,
            params={}
        ),
        BenchmarkCase(
            name="R(B4, B4)",
            goal=Goal(
                reward=-CountBooks(4, 4)
            ),
            goal_target=0,
            num_vertices=10,
            params={}
        ),
        BenchmarkCase(
            name="R(B3, B5)",
            goal=Goal(
                reward=-CountBooks(3, 5)
            ),
            goal_target=0,
            num_vertices=9,
            params={}
        ),
        BenchmarkCase(
            name="R(B4, B5)",
            goal=Goal(
                reward=-CountBooks(4, 5)
            ),
            goal_target=0,
            num_vertices=11,
            params={}
        ),
        BenchmarkCase(
            name="R(B5, B5)",
            goal=Goal(
                reward=-CountBooks(5, 5)
            ),
            goal_target=0,
            num_vertices=14,
            params={}
        ),
    ]
