from typing import Optional, Tuple

import pytest

from src.binary_tree.node import Node
from src.binary_tree.tree_min import tree_min_value, tree_min_value_breadth_first, tree_min_value_depth_first_recursive


def param_0() -> Tuple[Optional[Node], float]:
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
    return a, -2

def param_1() -> Tuple[Optional[Node], float]:
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f 
    return a, 3

def param_2() -> Tuple[Optional[Node], float]:
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h   
    return a, -13

def param_3() -> Tuple[Optional[Node], float]:
     return Node(42), 42

@pytest.mark.parametrize(
    "params",
    [
        (param_0()),
        (param_1()),
        (param_2()),
        (param_3())
    ]
)
def test_tree_min(params: Tuple[Optional[Node], float]):
    assert tree_min_value(params[0]) == params[1]
    assert tree_min_value_breadth_first(params[0]) == params[1]
    assert tree_min_value_depth_first_recursive(params[0]) == params[1]
