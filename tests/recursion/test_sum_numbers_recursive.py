import pytest

from src.recursion.sum_numbers_recursive import sum_numbers_recursive

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([5, 2, 9, 10], 26),
        ([1, -1, 1, -1, 1, -1, 1], 1),
        ([], 0),
        ([1000, 0, 0, 0, 0, 0, 1], 1001),
        ([700, 70, 7], 777),
        ([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -55),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0),
        ([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0], 137174205)
    ],
)
def test_sum_numbers_recursive(numbers: list[int], expected: int):
    assert sum_numbers_recursive(numbers) == expected
