from typing import List, Optional, Tuple

import pytest

from src.binary_tree.breadth_first_values import breadth_first_values
from src.binary_tree.node import Node


def param_0() -> Tuple[Optional[Node], List[str]]:
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
    return a, ["a", "b", "c", "d", "e", "f"]


def param_1() -> Tuple[Optional[Node], List[str]]:
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
    return a, ["a", "b", "c", "d", "e", "f", "g", "h"]


def param_2() -> Tuple[Optional[Node], List[str]]:
    return Node("a"), ["a"]


def param_3() -> Tuple[Optional[Node], List[str]]:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    x = Node("x")

    a.right = b
    b.left = c
    c.left = x
    c.right = d
    d.right = e
    return a, ["a", "b", "c", "x", "d", "e"]


def param_4() -> Tuple[Optional[Node], List[str]]:
    return None, []


@pytest.mark.parametrize(
    "params",
    [
        (param_0()),
        (param_1()),
        (param_2()),
        (param_3()),
        (param_4()),
    ],
)
def test_breadth_first_values(params: Tuple[Optional[Node], List[str]]):
    assert breadth_first_values(params[0]) == params[1]
