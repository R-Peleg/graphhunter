from dataclasses import dataclass
from typing import Any, Optional
from graphhunter.api import Goal

@dataclass
class BenchmarkCase:
    """Represents a single benchmark configuration."""
    name: str
    goal: Goal
    # If specified, gets a score of success/failure for the search
    goal_target: Optional[float] = None
    num_vertices: int
    params: dict[str, Any]

    def __str__(self) -> str:
        return f"Benchmark: {self.name} (vertices: {self.num_vertices})"
