from typing import Any, List, Optional

import pytest

from src.binary_tree.leaf_list import leaf_list, leaf_list_iterative
from src.binary_tree.node import Node


def param_0() -> Optional[Node]:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def param_1() -> Optional[Node]:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    return a


def param_2() -> Optional[Node]:
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


def param_3() -> Optional[Node]:
    return Node("x")


def param_4() -> Optional[Node]:
    return None


@pytest.mark.parametrize(
    "root, expected",
    [
        (param_0(), ["d", "e", "f"]),
        (param_1(), ["d", "g", "h"]),
        (param_2(), [20, 1, 3, 54]),
        (param_3(), ["x"]),
        (param_4(), []),
    ],
)
def test_leaf_list(root: Optional[Node], expected: List[Any]):
    assert leaf_list(root) == expected
    assert leaf_list_iterative(root) == expected
