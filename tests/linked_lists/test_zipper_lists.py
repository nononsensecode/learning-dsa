import pytest

from src.linked_lists.node import Node
from src.linked_lists.zipper_list import zipper_lists


def param0() -> tuple[Node, Node]:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    return a, x


def param0_zipper() -> Node:
    a = Node("a")
    b = Node("b")
    c = Node("c")

    x = Node("x")
    y = Node("y")
    z = Node("z")

    a.next = x
    x.next = b
    b.next = y
    y.next = c
    c.next = z

    return a


def param1() -> tuple[Node, Node]:
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

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    return a, x


def param1_zipper() -> Node:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    x = Node("x")
    y = Node("y")
    z = Node("z")
    a.next = x
    x.next = b
    b.next = y
    y.next = c
    c.next = z
    z.next = d
    d.next = e
    e.next = f

    return a


def param2() -> tuple[Node, Node]:
    s = Node("s")
    t = Node("t")
    s.next = t
    # s -> t

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.next = two
    two.next = three
    three.next = four
    return s, one


def param2_zipper() -> Node:
    s = Node("s")
    t = Node("t")
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)

    s.next = one
    one.next = t
    t.next = two
    two.next = three
    three.next = four

    return s


def param3() -> tuple[Node, Node]:
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3

    w = Node("w")
    return one, w


def param3_zipper() -> Node:
    one = Node(1)
    two = Node(2)
    three = Node(3)
    w = Node("w")
    one.next = w
    w.next = two
    two.next = three
    return one


@pytest.mark.parametrize(
    "heads, expected",
    [
        (param0(), param0_zipper()),
        (param1(), param1_zipper()),
        (param2(), param2_zipper()),
        (param3(), param3_zipper()),
    ],
)
def test_zipper_list(heads: tuple[Node, Node], expected: Node):
    assert zipper_lists(head_1=heads[0], head_2=heads[1]) == expected
