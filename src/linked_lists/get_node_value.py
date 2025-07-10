from typing import Optional

from .node import Node

# def get_node_value(a: Optional[Node], index: int) -> Optional[str]:
#     count = 0
#     current = a
#     while current is not None:
#         if index == count:
#             return current.val

#         count += 1
#         current = current.next

#     return None


def get_node_value(a: Optional[Node], index: int) -> Optional[str]:
    return _get_node_value(a, index, 0)


def _get_node_value(a: Optional[Node], index: int, count: int) -> Optional[str]:
    if a == None:
        return None

    if count == index:
        return a.val

    count += 1
    return _get_node_value(a.next, index, count)


# Time complexity: O(n)
# Space complexity: O(n) if we use recursion else O(1)
