from typing import Optional

from src.linked_lists.node import Node

# def linked_list_find(n: Node, s: str) -> bool:
#     current = n
#     while current is not None:
#         if s == current.val:
#             return True
#         current = current.next

#     return False


def linked_list_find(n: Optional[Node], s: str) -> bool:
    if n == None:
        return False

    if n.val == s:
        return True

    return linked_list_find(n.next, s)


# Time Complexity: O(n)
# Space Complexity: O(n) if the solution is recursion based, else O(1)
