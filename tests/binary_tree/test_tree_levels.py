from typing import List, Optional

import pytest

from src.binary_tree.node import Node
from src.binary_tree.tree_levels import tree_levels, tree_levels_recursive


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
    return None


@pytest.mark.parametrize(
    "root, expected",
    [
        (param_0(), [["a"], ["b", "c"], ["d", "e", "f"]]),
        (param_1(), [["a"], ["b", "c"], ["d", "e", "f"], ["g", "h", "i"]]),
        (param_2(), [["q"], ["r", "s"], ["t"], ["u"], ["v"]]),
        (param_3(), []),
    ],
)
def test_tree_levels(root: Optional[Node], expected: List[List[str]]):
    assert tree_levels(root) == expected
    assert tree_levels_recursive(root) == expected
