import pytest

from src.recursion.factorial import factorial


@pytest.mark.parametrize(
    "number, expected",
    [
        (3, 6),
        (6, 720),
        (18, 6402373705728000),
        (1, 1),
        (13, 6227020800),
        (0, 1)
    ],
)
def test_sum_numbers_recursive(number: int, expected: int):
    assert factorial(number) == expected