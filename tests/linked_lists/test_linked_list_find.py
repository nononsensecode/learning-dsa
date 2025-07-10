import pytest

from src.linked_lists.linked_list_find import linked_list_find
from src.linked_lists.node import Node


def param1() -> Node:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d
    return a


def param2() -> Node:
    node1 = Node("jason")
    node2 = Node("leneli")

    node1.next = node2
    return node1


def param5() -> Node:
    return Node(42)


@pytest.mark.parametrize(
    "head, target, expected",
    [
        (param1(), "c", True),
        (param1(), "d", True),
        (param1(), "q", False),
        (param2(), "jason", True),
        (param5(), 42, True),
        (param5(), 100, False),
    ],
)
def test_linked_list_find(head: Node, target: str, expected: bool):
    assert linked_list_find(head, target) == expected
