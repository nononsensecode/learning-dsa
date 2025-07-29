from typing import Dict, List

import pytest

from src.graph.connected_components_count import connected_components_count


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
            2,
        ),
        ({1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}, 1),
        ({3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}, 3),
        ({}, 0),
        ({0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}, 5),
    ],
)
def test_connected_components_count(graph: Dict[str, List[str]], expected: int):
    assert connected_components_count(graph) == expected
