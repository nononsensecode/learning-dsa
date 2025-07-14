from typing import Any, Optional

from .node import Node


def is_univalue_list(n: Optional[Node], prev_val: Optional[Any] = None) -> bool:
    if n is None:
        return True

    # In the first recursion, we need to skip this checking
    # Then only prev_val will be set
    if n.val != prev_val and prev_val is not None:
        return False

    return is_univalue_list(n.next, n.val)


# def is_univalue_list(n: Node) -> bool:
#     current = n.next
#     first_val = n.val
#     while current is not None:
#         if first_val != current.val:
#             return False

#         current = current.next

#     return True

# Time Complexity: O(n)
# Space Complexity: In the case of loop, it is O(1). In the case of recursion, it is O(n)
