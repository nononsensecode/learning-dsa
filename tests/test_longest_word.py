import pytest

from src.longest_word import longest_word


@pytest.mark.parametrize(
    "sentence, expected_longest_word",
    [
        ("what a wonderful world", "wonderful"),
        ("have a nice day", "nice"),
        ("the quick brown fox jumped over the lazy dog", "jumped"),
        ("who did eat the ham", "ham"),
        ("potato", "potato"),
    ],
)
def test_longest_word(sentence: str, expected_longest_word: str):
    assert longest_word(sentence) == expected_longest_word
