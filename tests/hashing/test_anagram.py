import pytest

from src.hashing.anagrams import anagrams


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ('restful', 'fluster', True),
        ('cats', 'tocs', False),
        ('monkeyswrite', 'newyorktimes', True),
        ('paper', 'reapa', False),
        ('elbow', 'below', True),
        ('tax', 'taxi', False),
        ('taxi', 'tax', False),
        ('night', 'thing', True),
        ('abbc', 'aabc', False),
        ('po', 'popp', False),
        ('pp', 'oo', False),
    ],
)
def test_anagrams(s1: str, s2: str, expected: bool):
    assert anagrams(s1, s2) == expected
