import pytest

from src.hashing.exclusive_items import exclusive_items


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([4,2,1,6], [3,6,9,2,10], [4,1,3,9,10]),
        ([2,4,6], [4,2], [6]),
        ([4,2,1], [1,2,4,6], [6]),
        ([0,1,2], [10,11], [0,1,2,10,11]),
        ([ i for i in range(0, 50000) ], [ i for i in range(0, 50000) ], []),
    ],
)
def test_exclusive_items(a: list[int], b: list[int], expected: list[int]):
    assert sorted(exclusive_items(a, b)) == sorted(expected)
