from typing import Optional, Tuple

import pytest

from src.binary_tree.node import Node
from src.binary_tree.tree_includes import (
    tree_includes_breadth_vise,
    tree_includes_depth_vise,
    tree_includes_depth_vise_recursive,
)


def param_0() -> Tuple[Optional[Node], bool]:
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
    return a, True


def param_1() -> Tuple[Optional[Node], bool]:
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
    return a, True


def param_2() -> Tuple[Optional[Node], bool]:
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
    return a, False


def param_3() -> Tuple[Optional[Node], bool]:
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
    return a, True


def param_4() -> Tuple[Optional[Node], bool]:
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
    return a, False


def param_5() -> Tuple[Optional[Node], bool]:
    return None, False


@pytest.mark.parametrize(
    "params, target",
    [
        (param_0(), "e"),
        (param_1(), "a"),
        (param_2(), "n"),
        (param_3(), "f"),
        (param_4(), "p"),
        (param_5(), "b"),
    ],
)
def test_tree_includes(params: Tuple[Optional[Node], bool], target: str):
    assert tree_includes_depth_vise(params[0], target) == params[1]
    assert tree_includes_breadth_vise(params[0], target) == params[1]
    assert tree_includes_depth_vise_recursive(params[0], target) == params[1]
