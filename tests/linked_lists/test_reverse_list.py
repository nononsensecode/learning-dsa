from src.linked_lists.node import Node
from typing import Optional
from src.linked_lists.get_reverse_list import reverse_list
import pytest


def param1() -> Node:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    return a

def param2() -> Node:
    x = Node("x")
    y = Node("y")

    x.next = y    
    return x

def param3() -> Node:
    return Node("p")

@pytest.mark.parametrize(
    "node, expected",
    [
        (param1(), )
    ]
)