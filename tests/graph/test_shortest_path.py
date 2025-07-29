from typing import Dict, List

import pytest

from src.graph.shortest_path import shortest_path


@pytest.mark.parametrize(
    "edges, src, dst, expected",
    [
        ([["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]], "w", "z", 2),
        ([["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]], "y", "x", 1),
        (
            [
                ["a", "c"],
                ["a", "b"],
                ["c", "b"],
                ["c", "d"],
                ["b", "d"],
                ["e", "d"],
                ["g", "f"],
            ],
            "a",
            "e",
            3,
        ),
        (
            [
                ["a", "c"],
                ["a", "b"],
                ["c", "b"],
                ["c", "d"],
                ["b", "d"],
                ["e", "d"],
                ["g", "f"],
            ],
            "e",
            "c",
            2,
        ),
        (
            [
                ["a", "c"],
                ["a", "b"],
                ["c", "b"],
                ["c", "d"],
                ["b", "d"],
                ["e", "d"],
                ["g", "f"],
            ],
            "b",
            "g",
            -1,
        ),
        (
            [
                ["c", "n"],
                ["c", "e"],
                ["c", "s"],
                ["c", "w"],
                ["w", "e"],
            ],
            "w",
            "e",
            1,
        ),
        (
            [
                ["c", "n"],
                ["c", "e"],
                ["c", "s"],
                ["c", "w"],
                ["w", "e"],
            ],
            "n",
            "e",
            2,
        ),
        (
            [
                ["m", "n"],
                ["n", "o"],
                ["o", "p"],
                ["p", "q"],
                ["t", "o"],
                ["r", "q"],
                ["r", "s"],
            ],
            "m",
            "s",
            6,
        ),
    ],
)
def test_shortest_path(edges: List[List[str]], src: str, dst: str, expected: int):
    assert shortest_path(edges, src, dst) == expected
