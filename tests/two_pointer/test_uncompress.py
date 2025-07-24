from src.two_pointer.uncompress import uncompress, uncompress_two_pointer, uncompress_recursive
import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("2c3a1t", "ccaaat"),
        ("4s2b", "ssssbb"),
        ("2p1o5p", "ppoppppp"),
        ("3n12e2z", "nnneeeeeeeeeeeezz"),
        (
            "127y",
            "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
        ),
    ],
)
def test_uncompress(s: str, expected: str):
    assert uncompress(s) == expected
    assert uncompress_two_pointer(s) == expected
    assert uncompress_recursive(s) == expected
