import pytest

from src.hashing.pair_product import pair_product


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([3, 2, 5, 4, 1], 8, (1, 3)),
        ([3, 2, 5, 4, 1], 10, (1, 2)),
        ([4, 7, 9, 2, 5, 1], 5, (4, 5)),
        ([4, 7, 9, 2, 5, 1], 35, (1, 4)),
        ([3, 2, 5, 4, 1], 10, (1, 2)),
        ([4,6,8,2], 16, (2,3)),
        ( [i for i in range(1, 6001)], 35994000, (5998, 5999))
    ],
)
def test_pair_product(numbers: list[int], target: int, expected: tuple[int, int]):
    assert pair_product(numbers, target) == expected
