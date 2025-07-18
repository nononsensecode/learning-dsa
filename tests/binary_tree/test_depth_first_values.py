from typing import List, Optional, Tuple

import pytest

from src.binary_tree.depth_first_values import (
    depth_first_values,
    depth_first_values_recursive,
    depth_first_values_recursive_improved,
)
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
    return a, ["a", "b", "d", "e", "c", "f"]


def param_1() -> Tuple[Optional[Node], List[str]]:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    return a, ["a", "b", "d", "e", "g", "c", "f"]


def param_2() -> Tuple[Optional[Node], List[str]]:
    return Node("a"), ["a"]


def param_3() -> Tuple[Optional[Node], List[str]]:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    a.right = b
    b.left = c
    c.right = d
    d.right = e
    return a, ["a", "b", "c", "d", "e"]


def param_4() -> Tuple[Optional[Node], List[str]]:
    return None, []


@pytest.mark.parametrize(
    "params", [(param_0()), (param_1()), (param_2()), (param_3()), (param_4())]
)
def test_depth_first_values(params: Tuple[Optional[Node], List[str]]):
    assert depth_first_values(params[0]) == params[1]
    assert depth_first_values_recursive(params[0]) == params[1]
    assert depth_first_values_recursive_improved(params[0], []) == params[1]
