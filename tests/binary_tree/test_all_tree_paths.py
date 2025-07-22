from typing import Any, List, Optional

import pytest

from src.binary_tree.all_tree_paths import all_tree_paths
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
    i = Node("i")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i
    return a


def param_2() -> Optional[Node]:
    q = Node("q")
    r = Node("r")
    s = Node("s")
    t = Node("t")
    u = Node("u")
    v = Node("v")

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v
    return q


def param_3() -> Optional[Node]:
    return Node("z")


@pytest.mark.parametrize(
    "root, expected",
    [
        (param_0(), [["a", "b", "d"], ["a", "b", "e"], ["a", "c", "f"]]),
        (
            param_1(),
            [
                ["a", "b", "d"],
                ["a", "b", "e", "g"],
                ["a", "b", "e", "h"],
                ["a", "c", "f", "i"],
            ],
        ),
        (param_2(), [["q", "r", "t", "u", "v"], ["q", "s"]]),
        (param_3(), [["z"]]),
    ],
)
def test_all_tree_paths(root: Optional[Node], expected: List[List[Any]]):
    assert all_tree_paths(root) == expected
