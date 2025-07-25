from typing import List

import pytest

from src.two_pointer.five_sort import five_sort


def param_06() -> List[int]:
    fours = [4] * 20000
    fives = [5] * 20000
    nums = fours + fives
    return nums


@pytest.mark.parametrize(
    "input, expected",
    [
        ([5, 0], [0, 5]),
        ([12, 5, 1, 5, 12, 7], [12, 7, 1, 12, 5, 5]),
        ([5, 2, 5, 6, 5, 1, 10, 2, 5, 5], [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]),
        ([5, 5, 5, 1, 1, 1, 4], [4, 1, 1, 1, 5, 5, 5]),
        ([5, 5, 6, 5, 5, 5, 5], [6, 5, 5, 5, 5, 5, 5]),
        (
            [5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5],
            [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5],
        ),
        (param_06(), param_06()),
    ],
)
def test_five_sort(input: List[int], expected: List[int]):
    assert five_sort(input) == expected
