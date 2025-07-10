from typing import Optional

from .node import Node

# def sum_list(ll: Node) -> int:
#     sum = 0
#     current = ll
#     while current is not None:
#         sum += current.val
#         current = current.next
#     return sum


def sum_list(ll: Optional[Node]) -> int:
    if ll is None:
        return 0

    return ll.val + sum_list(ll.next)


# Time Complexity: O(n)
# Space Complexity: O(n) - In the case of recursive solution
# Space Complexity: O(1) - In the case of normal loop
