from typing import Optional

from .node import Node

# def merge_lists(head_1: Optional[Node], head_2: Optional[Node]) -> Optional[Node]:
#     current_1 = head_1
#     current_2 = head_2

#     dummy_head = Node(val=0)
#     tail = dummy_head

#     while current_1 is not None and current_2 is not None:
#         if current_1.val > current_2.val:
#             tail.next = current_2
#             current_2 = current_2.next
#         else:
#             tail.next = current_1
#             current_1 = current_1.next
#         tail = tail.next

#     if current_1 is not None:
#         tail.next = current_1

#     if current_2 is not None:
#         tail.next = current_2

#     return dummy_head.next


def merge_lists(head_1: Optional[Node], head_2: Optional[Node]) -> Optional[Node]:
    if head_1 is None and head_2 is None:
        return None

    if head_1 is None:
        return head_2

    if head_2 is None:
        return head_1

    if head_1.val > head_2.val:
        next = head_2.next
        head_2.next = merge_lists(head_1, next)
        return head_2
    else:
        next = head_1.next
        head_1.next = merge_lists(next, head_2)
        return head_1


# Space complexity: O(1). In the case of recursion, O(min(m,n))
# Time complexity: O(min(m,n))
