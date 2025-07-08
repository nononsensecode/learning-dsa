import pytest

from src.fizz_buzz import fizz_buzz


@pytest.mark.parametrize(
    "num, expected",
    [
        (11, [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11]),
        (2, [1, 2]),
        (
            16,
            [
                1,
                2,
                "fizz",
                4,
                "buzz",
                "fizz",
                7,
                8,
                "fizz",
                "buzz",
                11,
                "fizz",
                13,
                14,
                "fizzbuzz",
                16,
            ],
        ),
        (
            32,
            [
                1,
                2,
                "fizz",
                4,
                "buzz",
                "fizz",
                7,
                8,
                "fizz",
                "buzz",
                11,
                "fizz",
                13,
                14,
                "fizzbuzz",
                16,
                17,
                "fizz",
                19,
                "buzz",
                "fizz",
                22,
                23,
                "fizz",
                "buzz",
                26,
                "fizz",
                28,
                29,
                "fizzbuzz",
                31,
                32,
            ],
        ),
    ],
)
def test_fizz_buzz(num: int, expected: list[str]):
    assert fizz_buzz(num) == expected
