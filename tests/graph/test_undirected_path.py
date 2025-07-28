from typing import Dict, List, Tuple

import pytest

from src.graph.undirected_path import undirected_path


@pytest.mark.parametrize(
    "edges, node_A, node_B, expected",
    [
        ([("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")], "j", "m", True),
        ([("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")], "m", "j", True),
        ([("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")], "l", "j", True),
        ([("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")], "k", "o", False),
        ([("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")], "i", "o", False),
        (
            [
                ("b", "a"),
                ("c", "a"),
                ("b", "c"),
                ("q", "r"),
                ("q", "s"),
                ("q", "u"),
                ("q", "t"),
            ],
            "a",
            "b",
            True,
        ),
        (
            [
                ("b", "a"),
                ("c", "a"),
                ("b", "c"),
                ("q", "r"),
                ("q", "s"),
                ("q", "u"),
                ("q", "t"),
            ],
            "a",
            "c",
            True,
        ),
        (
            [
                ("b", "a"),
                ("c", "a"),
                ("b", "c"),
                ("q", "r"),
                ("q", "s"),
                ("q", "u"),
                ("q", "t"),
            ],
            "r",
            "t",
            True,
        ),
        (
            [
                ("b", "a"),
                ("c", "a"),
                ("b", "c"),
                ("q", "r"),
                ("q", "s"),
                ("q", "u"),
                ("q", "t"),
            ],
            "r",
            "b",
            False,
        ),
        (
            [
                ("s", "r"),
                ("t", "q"),
                ("q", "r"),
            ],
            "r",
            "t",
            True,
        ),
    ],
)
def test_undirected_path(
    edges: List[Tuple[str, str]], node_A: str, node_B: str, expected: bool
):
    assert undirected_path(edges, node_A, node_B) == expected
