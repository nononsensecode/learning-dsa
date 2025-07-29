from typing import Dict, List

import pytest

from src.graph.largest_component import largest_component


@pytest.mark.parametrize(
    "graph, expected",
    [
        (
            {
                0: [8, 1, 5],
                1: [0],
                5: [0, 8],
                8: [0, 5],
                2: [3, 4],
                3: [2, 4],
                4: [3, 2],
            },
            4,
        ),
        ({1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}, 6),
        ({3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}, 5),
        ({}, 0),
        ({0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}, 3),
    ],
)
def test_largest_component(graph: Dict[str, List[str]], expected: int):
    assert largest_component(graph) == expected
