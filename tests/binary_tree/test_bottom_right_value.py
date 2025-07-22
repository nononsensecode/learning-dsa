from typing import Optional, Any

import pytest

from src.binary_tree.bottom_right_value import bottom_right_value
from src.binary_tree.node import Node


def param_0() -> Optional[Node]:
    a = Node(3)
    b = Node(11)
    c = Node(10)
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
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    return a


def param_2() -> Optional[Node]:
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    i = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i
    return a


def param_3() -> Optional[Node]:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.right = d
    d.left = e
    e.right = f
    return a


def param_4() -> Optional[Node]:
    return Node(42)

@pytest.mark.parametrize(
    "root, expected",
    [
        (param_0(), 1),
        (param_1(), 6),
        (param_2(), 7),
        (param_3(), "f"),
        (param_4(), 42),
    ]
)
def test_bottom_right_value(root: Optional[Node], expected: Any):
    assert bottom_right_value(root) == expected
