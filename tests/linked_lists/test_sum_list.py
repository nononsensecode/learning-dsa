import pytest

from src.linked_lists.node import Node
from src.linked_lists.sum_list import sum_list


def param1() -> Node:
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    return a


def param2() -> Node:
    x = Node(38)
    y = Node(4)

    x.next = y
    return x


def param3() -> Node:
    return Node(100)


@pytest.mark.parametrize(
    "head, expected", [(param1(), 19), (param2(), 42), (param3(), 100), (None, 0)]
)
def test_sum_list(head: Node, expected: int):
    assert sum_list(head) == expected
