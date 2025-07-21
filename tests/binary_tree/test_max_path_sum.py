from typing import Optional, Tuple

import pytest

from src.binary_tree.max_path_sum import max_path_sum
from src.binary_tree.node import Node


def param_0() -> Tuple[Optional[Node], int]:
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
    return a, 18


def param_1() -> Tuple[Optional[Node], int]:
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
    return a, 59


def param_2() -> Tuple[Optional[Node], int]:
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(-13)
    g = Node(-1)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    return a, -8


def param_3() -> Tuple[Optional[Node], int]:
    return Node(42), 42


@pytest.mark.parametrize("params", [(param_0()), (param_1()), (param_2()), (param_3())])
def test_max_path_sum(params: Tuple[Optional[Node], int]):
    assert max_path_sum(params[0]) == params[1]
