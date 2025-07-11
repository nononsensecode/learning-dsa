from typing import Optional

from .node import Node


def reverse_list(n: Node) -> Optional[Node]:
    current = n
    prev: Optional[Node] = None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


# def reverse_list(n: Node, prev: Optional[Node]=None) -> Optional[Node]:
#     if n is None:
#         return n

#     next = n.next
#     n.next = prev
#     return reverse_list(next, n)


# Time Complexity: O(n)
# Space Complexity: O(1) if we use loop, if we use recursion then O(n)
