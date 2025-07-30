from typing import List, Set, Tuple

import pytest

from src.graph.minimum_island import minimum_island


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
            2,
        ),
        (
            [
                ["L", "W", "W", "L", "W"],
                ["L", "W", "W", "L", "L"],
                ["W", "L", "W", "L", "W"],
                ["W", "W", "W", "W", "W"],
                ["W", "W", "L", "L", "L"],
            ],
            1,
        ),
        (
            [
                ["L", "L", "L"],
                ["L", "L", "L"],
                ["L", "L", "L"],
            ],
            9,
        ),
        ([["W", "W"], ["L", "L"], ["W", "W"], ["W", "L"]], 1),
    ],
)
def test_minimum_island(grid: List[List[str]], expected: int):
    assert minimum_island(grid) == expected
