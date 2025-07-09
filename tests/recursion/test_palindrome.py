import pytest

from src.recursion.palindrome import palindrome


@pytest.mark.parametrize(
    "string, expected",
    [
        ("pop", True),
        ("kayak", True),
        ("pops", False),
        ("boot", False),
        ("rotator", True),
        ("abcbca", False),
        ("", True)
    ],
)
def test_palindrome(string: str, expected: bool):
    assert palindrome(string) == expected