import pytest
from src.linked_lists.node import Node
from src.linked_lists.get_node_value import get_node_value
from typing import Optional


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
    node1 = Node("banana")
    node2 = Node("mango")

    node1.next = node2
    return node1


@pytest.mark.parametrize(
    "node, index, expected",
    [
        (param1(), 2, "c"),
        (param1(), 3, "d"),
        (param1(), 7, None),
        (param2(), 0, "banana"),
        (param2(), 1, "mango"),
    ],
)
def test_get_node_value(node: Node, index: int, expected: Optional[str]):
    assert get_node_value(node, index) == expected
