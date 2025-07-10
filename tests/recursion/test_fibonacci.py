import pytest

from src.recursion.fibonacci import fibonacci


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (8, 21),
    ],
)
def test_fibonacci(number: int, expected: int):
    assert fibonacci(number) == expected