import pytest
from src.binary_tree.node import Node
from src.binary_tree.how_high import how_high
from typing import Optional

def param_0() -> Optional[Node]:
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f  
    return a

def param_1() -> Optional[Node]  :
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    return a

def param_2() -> Optional[Node]:
    a = Node('a')
    c = Node('c')

    a.right = c    
    return a

def param_3() -> Optional[Node]:
    return Node('a')

def param_4() -> Optional[Node]:
    return None

@pytest.mark.parametrize(
    "root, expected",
    [
        (param_0(), 2),
        (param_1(), 3),
        (param_2(), 1),
        (param_3(), 0),
        (param_4(), -1),
    ]
)
def test_how_high(root: Optional[Node], expected: int):
    assert how_high(root) == expected