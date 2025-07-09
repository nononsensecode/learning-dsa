import pytest

from src.hashing.most_frequent_char import most_frequent_char


@pytest.mark.parametrize(
    "string, expected",
    [
        ('bookeeper', 'e'),
        ('david', 'd'),
        ('abby', 'b'),
        ('mississippi', 'i'),
        ('potato', 'o'),
        ('eleventennine', 'e'),
        ('riverbed', 'r'),
    ],
)
def test_most_frequent_char(string: str, expected: bool):
    assert most_frequent_char(string) == expected
