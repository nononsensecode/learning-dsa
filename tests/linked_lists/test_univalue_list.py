from src.linked_lists.node import Node
from src.linked_lists.is_univalue_list import is_univalue_list
import pytest


def param_0() -> Node:
    a = Node(7)
    b = Node(7)
    c = Node(7)

    a.next = b
    b.next = c
    return a


def param_1() -> Node:
    a = Node(7)
    b = Node(7)
    c = Node(4)

    a.next = b
    b.next = c
    return a


def param_2() -> Node:
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y
    return u


def param_3() -> Node:
    u = Node(2)
    v = Node(2)
    w = Node(3)
    x = Node(3)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y
    return u


def param_4() -> Node:
    return Node("z")


def param_5() -> Node:
    u = Node(2)
    v = Node(1)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y
    return u


@pytest.mark.parametrize(
    "head, expected",
    [
        (param_0(), True),
        (param_1(), False),
        (param_2(), True),
        (param_3(), False),
        (param_4(), True),
        (param_5(), False),
    ],
)
def test_is_univalue_list(head: Node, expected: bool):
    assert is_univalue_list(head) == expected
