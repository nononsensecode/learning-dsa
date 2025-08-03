from typing import Dict, List

import pytest

from src.graph.longest_path import longest_path


@pytest.mark.parametrize(
    "graph, expected",
    [
        ({"a": ["c", "b"], "b": ["c"], "c": []}, 2),
        (
            {
                "a": ["c", "b"],
                "b": ["c"],
                "c": [],
                "q": ["r"],
                "r": ["s", "u", "t"],
                "s": ["t"],
                "t": ["u"],
                "u": [],
            },
            4,
        ),
        (
            {
                "h": ["i", "j", "k"],
                "g": ["h"],
                "i": [],
                "j": [],
                "k": [],
                "x": ["y"],
                "y": [],
            },
            2,
        ),
        (
            {
                "a": ["b"],
                "b": ["c"],
                "c": [],
                "e": ["f"],
                "f": ["g"],
                "g": ["h"],
                "h": [],
            },
            3,
        ),
        (
            {
                "a": [
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                ],
                "b": ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
                "c": ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
                "d": ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
                "e": ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
                "f": [
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                ],
                "g": ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
                "h": ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
                "i": ["j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
                "j": ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"],
                "k": ["l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"],
                "l": ["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"],
                "m": ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"],
                "n": ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                "o": ["p", "q", "r", "s", "t", "u", "v", "w", "x"],
                "p": ["q", "r", "s", "t", "u", "v", "w", "x", "y"],
                "q": ["r", "s", "t", "u", "v", "w", "x", "y"],
                "r": ["s", "t", "u", "v", "w", "x", "y", "z"],
                "s": ["t", "u", "v", "w", "x", "y", "z"],
                "t": ["u", "v", "w", "x", "y", "z"],
                "u": ["v", "w", "x", "y", "z"],
                "v": ["w", "x", "y", "z"],
                "w": ["x", "y", "z"],
                "x": ["y", "z"],
                "y": ["z"],
                "z": [],
            },
            25,
        ),
    ],
)
def test_longest_path(graph: Dict[str, List[str]], expected: int):
    assert longest_path(graph) == expected
