from typing import List, Optional

import pytest

from src.binary_tree.level_averages import level_averages, level_averages_iterative
from src.binary_tree.node import Node


def param_0() -> Optional[Node]:
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def param_1() -> Optional[Node]:
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g
    return a


def param_2() -> Optional[Node]:
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(45)
    g = Node(-1)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    return a


def param_3() -> Optional[Node]:
    q = Node(13)
    r = Node(4)
    s = Node(2)
    t = Node(9)
    u = Node(2)
    v = Node(42)

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v
    return q


def param_4() -> Optional[Node]:
    return None


@pytest.mark.parametrize(
    "root, expected",
    [
        (param_0(), [3, 7.5, 1]),
        (param_1(), [5, 32.5, 17.5, 2]),
        (param_2(), [-1, -5.5, 14, -1.5]),
        (param_3(), [13, 3, 9, 2, 42]),
        (param_4(), []),
    ],
)
def test_level_averages(root: Optional[Node], expected: List[float]):
    assert level_averages(root) == expected
    assert level_averages_iterative(root) == expected
