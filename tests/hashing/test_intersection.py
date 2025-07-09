import pytest

from src.hashing.intersection import intersection


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([4,2,1,6], [3,6,9,2,10], [2,6]),
        ([2,4,6], [4,2], [2,4]),
        ([4,2,1], [1,2,4,6], [1,2,4]),
        ([0,1,2], [10,11], []),
        ([ i for i in range(0, 50000) ], [ i for i in range(0, 50000) ], [ i for i in range(0, 50000) ]),
    ],
)
def test_intersection(a: list[int], b: list[int], expected: list[int]):
    assert sorted(intersection(a, b)) == sorted(expected)
