from typing import Tuple, List

import pytest

from src.graph.semesters_required import semesters_required


@pytest.mark.parametrize(
    "num_courses, courses, semesters",
    [
        (6, [(1, 2), (2, 4), (3, 5), (0, 5)], 3),
        (
                7,
                [
                    (4, 3),
                    (3, 2),
                    (2, 1),
                    (1, 0),
                    (5, 2),
                    (5, 6),
                ],
                5,
        ),
        (
                5,
                [
                    (1, 0),
                    (3, 4),
                    (1, 2),
                    (3, 2),
                ],
                2,
        ),
        (12, [], 1),
        (
                3,
                [
                    (0, 2),
                    (0, 1),
                    (1, 2),
                ],
                3,
        ),
        (
                6,
                [
                    (3, 4),
                    (3, 0),
                    (3, 1),
                    (3, 2),
                    (3, 5),
                ],
                2,
        ),
        (3, [(0, 1), (1, 2)], 3),
        (3, [], 1),
        (4, [(0, 1), (0, 2), (0, 3)], 2),
        (4, [(0, 1), (1, 2), (0, 3)], 3),
    ],
)
def test_semesters_required(
        num_courses: int, courses: List[Tuple[int, int]], semesters: int
):
    assert semesters_required(num_courses, courses) == semesters
