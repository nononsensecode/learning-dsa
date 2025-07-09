import pytest

from src.hashing.pair_sum import pair_sum


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([3, 2, 5, 4, 1], 8, (0,2)),
        ([4, 7, 9, 2, 5, 1], 5, (0, 5)),
        ([4, 7, 9, 2, 5, 1], 3, (3, 5)),
        ([1, 6, 7, 2], 13, (1, 2)),
        ([9, 9], 18,(0, 1)),
        ([6, 4, 2, 8 ], 12, (1, 3)),
        ([ i for i in range(1, 6001) ], 11999, (5998, 5999)),
    ],
)
def test_pair_sum(numbers: list[int], target: int, expected: tuple[int, int]):
    assert pair_sum(numbers, target) == expected
