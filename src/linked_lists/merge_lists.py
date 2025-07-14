from typing import Optional

from .node import Node


def merge_lists(head_1: Optional[Node], head_2: Optional[Node]) -> Optional[Node]:
    current_1 = head_1
    current_2 = head_2

    dummy_head = Node(val=0)
    tail = dummy_head

    while current_1 is not None and current_2 is not None:
        if current_1.val > current_2.val:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next

    if current_1 is not None:
        tail.next = current_1

    if current_2 is not None:
        tail.next = current_2

    return dummy_head.next


# Space complexity: O(1)
# Time complexity: O(min(m,n))
