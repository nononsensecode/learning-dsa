from typing import Optional

import pytest

from src.linked_lists.get_reverse_list import reverse_list
from src.linked_lists.node import Node


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


def param1_reverse() -> Node:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    f.next = e
    e.next = d
    d.next = c
    c.next = b
    b.next = a

    return f


def param2() -> Node:
    x = Node("x")
    y = Node("y")

    x.next = y
    return x


def param2_reverse() -> Node:
    x = Node("x")
    y = Node("y")

    y.next = x
    return y


def param3() -> Node:
    return Node("p")


@pytest.mark.parametrize(
    "node, expected",
    [(param1(), param1_reverse()), (param2(), param2_reverse()), (param3(), param3())],
)
def test_reverse_list(node: Node, expected: Node):
    assert reverse_list(node) == expected
