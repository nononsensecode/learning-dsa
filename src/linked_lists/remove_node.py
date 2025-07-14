from typing import Optional

from .node import Node

# def remove_node(head: Node, target_val: str) -> Node:
#     current = head
#     prev: Optional[Node] = None

#     while current is not None:
#         if target_val == current.val:
#             if prev is not None:
#                 prev.next = current.next
#                 break
#             head = head.next
#             break

#         prev = current
#         current = current.next

#     return head


def remove_node(head: Node, target_val: str, prev: Optional[Node] = None) -> Node:
    if head is None:
        return None

    if target_val == head.val:
        return head.next

    head.next = remove_node(head.next, target_val=target_val, prev=head)
    return head


# Time complexity: O(n)
# Space complexity: O(1) if we use looped solution. If we use recursive solution, O(n)
