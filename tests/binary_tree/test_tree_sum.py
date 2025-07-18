from typing import Optional, Tuple

import pytest

from src.binary_tree.node import Node
from src.binary_tree.tree_sum import (
    tree_sum_breadth_vise,
    tree_sum_depth_vise,
    tree_sum_depth_vise_recursive,
)


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
    return a, 21


def param_1() -> Tuple[Optional[Node], int]:
    a = Node(1)
    b = Node(6)
    c = Node(0)
    d = Node(3)
    e = Node(-6)
    f = Node(2)
    g = Node(2)
    h = Node(2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    return a, 10


def param_2() -> Tuple[Optional[Node], int]:
    return None, 0


@pytest.mark.parametrize("params", [(param_0()), (param_1()), (param_2())])
def test_tree_sum(params: Tuple[Optional[Node], int]):
    assert tree_sum_depth_vise(params[0]) == params[1]
    assert tree_sum_breadth_vise(params[0]) == params[1]
    assert tree_sum_depth_vise_recursive(params[0]) == params[1]
