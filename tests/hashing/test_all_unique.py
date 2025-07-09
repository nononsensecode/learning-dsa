import pytest

from src.hashing.all_unique import all_unique


@pytest.mark.parametrize(
    "items, expected",
    [
        (["q", "r", "s", "a"], True),
        (["q", "r", "s", "a", "r", "z"], False),
        (["red", "blue", "yellow", "green", "orange"], True),
        (["cat", "cat", "dog"], False),
        (["a", "u", "t", "u", "m", "n"], False),
    ],
)
def test_all_unique(items: list[str], expected: bool):
    assert all_unique(items) == expected