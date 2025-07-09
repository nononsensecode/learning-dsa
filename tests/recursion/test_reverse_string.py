import pytest

from src.recursion.reverse_string import reverse_string

@pytest.mark.parametrize(
    "string, expected",
    [
        ("hello", "olleh"),
        ('abcdefg', 'gfedcba'),
        ('stopwatch', 'hctawpots'),
        ("", ""),
    ],
)
def test_reverse_string(string: str, expected: str):
    assert reverse_string(string) == expected