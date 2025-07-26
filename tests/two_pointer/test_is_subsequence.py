from src.two_pointer.is_subsequence import is_subsequence
import pytest

@pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("bde", "abcdef", True),
            ("bda", "abcdef", False),
            ("ser", "super", True),
            ("serr", "super", False),
            ("ama", "camera", True),
            ("unfun", "unfortunate", True),
            ("riverbed", "river", False),
            ("river", "riverbed", True)
        ]
)
def test_is_subsequence(s1: str, s2: str, expected: bool):
    assert is_subsequence(s1, s2) == expected