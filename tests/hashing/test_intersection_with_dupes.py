import pytest

from src.hashing.intersection_with_dupes import intersection_with_dupes

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (
                ["a", "b", "c", "b"],
                ["x", "y", "b", "b"]
                , ["b", "b"]),
        (
                ["q", "b", "m", "s", "s", "s"],
                ["s", "m", "s"]
                , ["m", "s", "s"]),
        (
                ["p", "r", "r", "r"],
                ["r"]
                , ["r"]),
        (
                ["t", "v", "u"],
                ["g", "e", "d", "f"]
                , []),
        ([f"{i}" for i in range(0, 150000)], [f"{i}" for i in range(0, 150000)], [f"{i}" for i in range(0, 150000)]),
    ],
)
def test_intersection_with_dupes(a: list[str], b: list[str], expected: list[str]):
    assert intersection_with_dupes(a, b) == expected
