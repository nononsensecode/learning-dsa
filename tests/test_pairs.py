import pytest

from src.pairs import pairs


@pytest.mark.parametrize(
    "elements, expected_pairs",
    [
        (["a", "b", "c"], [["a", "b"], ["a", "c"], ["b", "c"]]),
        (
            ["a", "b", "c", "d"],
            [["a", "b"], ["a", "c"], ["a", "d"], ["b", "c"], ["b", "d"], ["c", "d"]],
        ),
        (
            ["cherry", "cranberry", "banana", "blueberry", "lime", "papaya"],
            [
                ["cherry", "cranberry"],
                ["cherry", "banana"],
                ["cherry", "blueberry"],
                ["cherry", "lime"],
                ["cherry", "papaya"],
                ["cranberry", "banana"],
                ["cranberry", "blueberry"],
                ["cranberry", "lime"],
                ["cranberry", "papaya"],
                ["banana", "blueberry"],
                ["banana", "lime"],
                ["banana", "papaya"],
                ["blueberry", "lime"],
                ["blueberry", "papaya"],
                ["lime", "papaya"],
            ],
        ),
    ],
)
def test_pairs(elements: list[str], expected_pairs: list[list[str]]):
    assert pairs(elements) == expected_pairs
