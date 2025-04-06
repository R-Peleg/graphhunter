from dataclasses import dataclass
from typing import Any
from graphhunter.api import Goal

@dataclass
class BenchmarkCase:
    """Represents a single benchmark configuration."""
    name: str
    goal: Goal
    num_vertices: int
    params: dict[str, Any]

    def __str__(self) -> str:
        return f"Benchmark: {self.name} (vertices: {self.num_vertices})"
