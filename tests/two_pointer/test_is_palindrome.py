from src.two_pointer.is_palindrome import is_palindrome, is_palindrome_iterative
import pytest

@pytest.mark.parametrize(
    "word, expected",
    [
        ("pop", True),
        ("kayak", True),
        ("pops", False),
        ("boot", False),
        ("rotator", True),
        ("abcbca", False),
        ("", True)
    ]
)
def test_is_palindrome(word: str, expected: bool):
    assert is_palindrome(word) == expected
    assert is_palindrome_iterative(word) == expected
