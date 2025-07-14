import pytest

from src.linked_lists.merge_lists import merge_lists
from src.linked_lists.node import Node, assert_equal


def param_0() -> tuple[Node, Node]:
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t
    # 6 -> 8 -> 9 -> 25

    return a, q


def param_0_merged() -> Node:
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    a.next = q
    q.next = b
    b.next = r
    r.next = s
    s.next = c
    c.next = d
    d.next = e
    e.next = t
    t.next = f

    return a


def param_1() -> tuple[Node, Node]:
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = r
    r.next = s
    s.next = t

    return a, q


def param_1_merged() -> Node:
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = a
    a.next = b
    b.next = r
    r.next = s
    s.next = t
    t.next = c
    c.next = d
    d.next = e
    e.next = f

    return q


def param_2() -> tuple[Node, Node]:
    h = Node(30)
    # 30

    p = Node(15)
    q = Node(67)
    p.next = q

    return h, p


def param_2_merged() -> Node:
    h = Node(30)
    p = Node(15)
    q = Node(67)
    p.next = h
    h.next = q
    return p


@pytest.mark.parametrize(
    "head_1, head_2, expected",
    [
        (param_0()[0], param_0()[1], param_0_merged()),
        (param_1()[0], param_1()[1], param_1_merged()),
        (param_2()[0], param_2()[1], param_2_merged()),
    ],
)
def test_merge_lists(head_1: Node, head_2: Node, expected: Node):
    assert merge_lists(head_1, head_2) == expected
