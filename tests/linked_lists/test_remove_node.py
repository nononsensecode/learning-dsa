from src.linked_lists.node import Node
from src.linked_lists.remove_node import remove_node
import pytest
from typing import Optional


def param_0() -> Node:
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


def param_0_removed() -> Node:
    a = Node("a")
    b = Node("b")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = d
    d.next = e
    e.next = f

    return a


def param_1() -> Node:
    x = Node("x")
    y = Node("y")
    z = Node("z")

    x.next = y
    y.next = z
    return x


def param_1_removed() -> Node:
    x = Node("x")
    y = Node("y")

    x.next = y
    return x


def param_2() -> Node:
    q = Node("q")
    r = Node("r")
    s = Node("s")

    q.next = r
    r.next = s
    return q


def param_2_removed() -> Node:
    r = Node("r")
    s = Node("s")

    r.next = s
    return r


def param_3() -> Node:
    node1 = Node("h")
    node2 = Node("i")
    node3 = Node("j")
    node4 = Node("i")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    return node1


def param_3_removed() -> Node:
    node1 = Node("h")
    node3 = Node("j")
    node4 = Node("i")

    node1.next = node3
    node3.next = node4
    return node1


def param_4() -> Node:
    return Node("t")


def param_4_removed() -> Optional[Node]:
    return None


@pytest.mark.parametrize(
    "head, target_val, expected",
    [
        (param_0(), "c", param_0_removed()),
        (param_1(), "z", param_1_removed()),
        (param_2(), "q", param_2_removed()),
        (param_3(), "i", param_3_removed()),
        (param_4(), "t", param_4_removed()),
    ],
)
def test_remove_node(head: Node, target_val: str, expected: Node):
    assert remove_node(head, target_val) == expected
