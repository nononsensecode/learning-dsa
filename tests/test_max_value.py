import pytest

from src.max_value import max_value


@pytest.mark.parametrize(
    "value_list, expected_max",
    [
        ([4, 7, 2, 8, 10, 9], 10),
        ([10, 5, 40, 40.3], 40.3),
        ([-5, -2, -1, -11], -1),
        ([42], 42),
        ([1000, 8], 1000),
        ([1000, 8, 9000], 9000),
        ([2, 5, 1, 1, 4], 5),
    ],
)
def test_max_value(value_list: list[int], expected_max: int):
    assert max_value(value_list) == expected_max
