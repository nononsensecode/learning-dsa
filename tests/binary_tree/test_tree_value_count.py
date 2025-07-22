from typing import Optional

import pytest

from src.binary_tree.node import Node
from src.binary_tree.tree_value_count import tree_value_count


def param_0() -> Optional[Node]:
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def param_1() -> Optional[Node]:
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def param_2() -> Optional[Node]:
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    return a


def param_3() -> Optional[Node]:
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    return a


def param_4() -> Optional[Node]:
    return None

@pytest.mark.parametrize(
    "root, target, expected",
    [
        (param_0(), 6, 3),
        (param_1(), 12, 2),
        (param_2(), 1, 4),
        (param_3(), 9, 0),
        (param_4(), 42, 0),
    ]
)
def test_tree_value_count(root: Optional[Node], target: str, expected: int):
    assert tree_value_count(root, target) == expected