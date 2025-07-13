from typing import Optional

from .node import Node

# def zipper_lists(head_1: Node, head_2: Node) -> Optional[Node]:
#     tail = head_1
#     current_1 = head_1.next
#     current_2 = head_2
#     take_from_second = True

#     while current_1 is not None and current_2 is not None:
#         if take_from_second:
#             tail.next = current_2
#             take_from_second = False
#             current_2 = current_2.next
#         else:
#             tail.next = current_1
#             take_from_second = True
#             current_1 = current_1.next
#         tail = tail.next

#     if current_1 is not None:
#         tail.next = current_1
#     if current_2 is not None:
#         tail.next = current_2

#     return head_1


def zipper_lists(head_1: Optional[Node], head_2: Optional[Node]) -> Optional[Node]:
    if head_1 is None and head_2 is None:
        return None

    if head_1 is None:
        return head_2

    if head_2 is None:
        return head_1

    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists(next_1, next_2)
    return head_1


# Space complexity: O(1) is we use loop, if we use recursion O(min(m,n))
# Time Complexity: O(min(m,n))
