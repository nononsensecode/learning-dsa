from typing import Optional

import pytest

from src.linked_lists.longest_streak import longest_streak
from src.linked_lists.node import Node


def param_0() -> Node:
    a = Node(5)
    b = Node(5)
    c = Node(7)
    d = Node(7)
    e = Node(7)
    f = Node(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    return a


def param_1() -> Node:
    a = Node(3)
    b = Node(3)
    c = Node(3)
    d = Node(3)
    e = Node(9)
    f = Node(9)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    return a


def param_2() -> Node:
    a = Node(9)
    b = Node(9)
    c = Node(1)
    d = Node(9)
    e = Node(9)
    f = Node(9)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    return a


def param_3() -> Node:
    a = Node(5)
    b = Node(5)

    a.next = b
    return a


def param_4() -> Node:
    return Node(4)


def param_5() -> Optional[Node]:
    return None


@pytest.mark.parametrize(
    "head, expected",
    [
        (param_0(), 3),
        (param_1(), 4),
        (param_2(), 3),
        (param_3(), 2),
        (param_4(), 1),
        (param_5(), 0),
    ],
)
def test_longest_streak(head: Node, expected: int):
    assert longest_streak(head) == expected
