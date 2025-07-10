from node import Node


def print_list(n: Node) -> None:
    if n.next is None:
        return

    print(n.val)
    print_list(n.next)


def print_list_by_loop(n: Node) -> None:
    current = n
    while current.next is not None:
        print(current.val)
        current = current.next


if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    a.next = b
    b.next = c
    c.next = d

    print_list(a)
    print("*" * 100)
    print_list_by_loop(a)
