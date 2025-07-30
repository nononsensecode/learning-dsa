from typing import List
from src.graph.island_count import island_count
import pytest


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["W", "L", "W", "W", "W"],
                ["W", "L", "W", "W", "W"],
                ["W", "W", "W", "L", "W"],
                ["W", "W", "L", "L", "W"],
                ["L", "W", "W", "L", "L"],
                ["L", "L", "W", "W", "W"],
            ],
            3,
        ),
        (
            [
                ["L", "W", "W", "L", "W"],
                ["L", "W", "W", "L", "L"],
                ["W", "L", "W", "L", "W"],
                ["W", "W", "W", "W", "W"],
                ["W", "W", "L", "L", "L"],
            ],
            4,
        ),
        (
            [
                ["L", "L", "L"],
                ["L", "L", "L"],
                ["L", "L", "L"],
            ],
            1,
        ),
        (
            [
                ["W", "W"],
                ["W", "W"],
                ["W", "W"],
            ], 0
        ),
    ],
)
def test_island_count(grid: List[List[str]], expected: int):
    assert island_count(grid) == expected
