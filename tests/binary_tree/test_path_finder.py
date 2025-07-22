from typing import List, Optional, Tuple

import pytest

from src.binary_tree.node import Node
from src.binary_tree.path_finder import path_finder


def param_0() -> Tuple[Optional[Node], Optional[List[str]]]:
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
    return a, ["a", "b", "e"]


def param_1() -> Tuple[Optional[Node], Optional[List[str]]]:
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
    return a, None


def param_2() -> Tuple[Optional[Node], Optional[List[str]]]:
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
    return a, ["a", "c"]


def param_3() -> Tuple[Optional[Node], Optional[List[str]]]:
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
    return a, ["a", "c", "f", "h"]


def param_4() -> Tuple[Optional[Node], Optional[List[str]]]:
    return Node("x"), ["x"]


@pytest.mark.parametrize(
    "params, target",
    [
        (param_0(), "e"),
        (param_1(), "p"),
        (param_2(), "c"),
        (param_3(), "h"),
        (param_4(), "x"),
    ],
)
def test_path_finder(params: Tuple[Optional[Node], Optional[List[str]]], target: str):
    assert path_finder(params[0], target) == params[1]
