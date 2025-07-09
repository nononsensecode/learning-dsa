import pytest

from src.recursion.sum_of_lengths import sum_of_lengths

@pytest.mark.parametrize(
    "strings, expected",
    [
        (['goat', 'cat', 'purple'], 13),
        (['bike', 'at', 'pencils', 'phone'], 18),
        ([], 0),
        (['', ' ', '  ', '   ', '    ', '     '], 15),
        (['0', '313', '1234567890'], 14),
    ],
)
def test_sum_of_lengths(strings: list[str], expected: int):
    assert sum_of_lengths(strings) == expected