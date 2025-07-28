from typing import Dict, List

import pytest

from src.graph.has_path import has_path, has_path_bread_first, has_path_recursive


@pytest.mark.parametrize(
    "graph, src, dst, expected",
    [
        (
            {
                "f": ["g", "i"],
                "g": ["h"],
                "h": [],
                "i": ["g", "k"],
                "j": ["i"],
                "k": [],
            },
            "f",
            "k",
            True,
        ),
        (
            {
                "f": ["g", "i"],
                "g": ["h"],
                "h": [],
                "i": ["g", "k"],
                "j": ["i"],
                "k": [],
            },
            "f",
            "j",
            False,
        ),
        (
            {
                "f": ["g", "i"],
                "g": ["h"],
                "h": [],
                "i": ["g", "k"],
                "j": ["i"],
                "k": [],
            },
            "i",
            "h",
            True,
        ),
        (
            {
                "v": ["x", "w"],
                "w": [],
                "x": [],
                "y": ["z"],
                "z": [],
            },
            "v",
            "w",
            True,
        ),
        (
            {
                "v": ["x", "w"],
                "w": [],
                "x": [],
                "y": ["z"],
                "z": [],
            },
            "v",
            "z",
            False,
        ),
    ],
)
def test_has_path(graph: Dict[str, List[str]], src: str, dst: str, expected: bool):
    assert has_path(graph, src, dst) == expected
    assert has_path_bread_first(graph, src, dst) == expected
    assert has_path_recursive(graph, src, dst) == expected
