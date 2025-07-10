import pytest
from src.linked_lists.linked_list_values import linked_list_values
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
    x = Node("x")
    y = Node("y")

    x.next = y
    return x


def param3() -> Node:
    q = Node("q")
    return q


@pytest.mark.parametrize(
    "head, expected",
    [
        (param1(), ["a", "b", "c", "d"]),
        (param2(), ["x", "y"]),
        (param3(), ["q"]),
        (None, []),
    ],
)
def test_linked_list_values(head: Node, expected: list[str]):
    assert linked_list_values(head) == expected
