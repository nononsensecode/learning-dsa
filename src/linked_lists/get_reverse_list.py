from typing import Optional

from .node import Node

# def reverse_list(n: Node) -> Optional[Node]:
#     current = n
#     prev: Optional[Node] = None

#     while current is not None:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next

#     return prev


def reverse_list(n: Node) -> Optional[Node]:
    return _reverse_list(n, None)


def _reverse_list(n: Optional[Node], prev: Optional[Node]) -> Optional[Node]:
    if n is None:
        return n

    next = n.next
    n.next = prev
    return _reverse_list(next, n)
