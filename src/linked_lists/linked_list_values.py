from typing import Optional

from .node import Node

# def linked_list_values(ll: Node) -> list[str]:
#     result = []
#     current = ll

#     while current is not None:
#         result.append(current.val)
#         current = current.next

#     return result


def linked_list_values(ll: Node) -> list[str]:
    result = []
    _linked_list_values(ll, result)
    return result


def _linked_list_values(ll: Optional[Node], start: list[str]):
    if ll is None:
        return None

    start.append(ll.val)
    _linked_list_values(ll.next, start)


# Time Complexity: O(n)
# Space Complexity: O(n)
