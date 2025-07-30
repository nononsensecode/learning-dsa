from typing import List

import pytest

from src.graph.closest_carrot import closest_carrot


@pytest.mark.parametrize(
    "grid, starting_row, starting_col, expected",
    [
        (
            [
                ["O", "O", "O", "O", "O"],
                ["O", "X", "O", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["O", "X", "C", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["C", "O", "O", "O", "O"],
            ],
            1,
            2,
            4,
        ),
        (
            [
                ["O", "O", "O", "O", "O"],
                ["O", "X", "O", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["O", "X", "C", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["C", "O", "O", "O", "O"],
            ],
            0,
            0,
            5,
        ),
        (
            [
                ["O", "O", "X", "X", "X"],
                ["O", "X", "X", "X", "C"],
                ["O", "X", "O", "X", "X"],
                ["O", "O", "O", "O", "O"],
                ["O", "X", "X", "X", "X"],
                ["O", "O", "O", "O", "O"],
                ["O", "O", "C", "O", "O"],
                ["O", "O", "O", "O", "O"],
            ],
            3,
            4,
            9,
        ),
        (
            [
                ["O", "O", "X", "O", "O"],
                ["O", "X", "X", "X", "O"],
                ["O", "X", "C", "C", "O"],
            ],
            1,
            4,
            2,
        ),
        (
            [
                ["O", "O", "X", "O", "O"],
                ["O", "X", "X", "X", "O"],
                ["O", "X", "C", "C", "O"],
            ],
            2,
            0,
            -1,
        ),
        (
            [
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "X", "C"],
            ],
            0,
            0,
            -1,
        ),
        (
            [
                ["O", "O", "X", "C", "O"],
                ["O", "X", "X", "X", "O"],
                ["C", "X", "O", "O", "O"],
            ],
            2,
            2,
            5,
        ),
    ],
)
def test_closest_carrot(
    grid: List[List[str]], starting_row: int, starting_col: int, expected: int
):
    assert closest_carrot(grid, starting_row, starting_col) == expected
