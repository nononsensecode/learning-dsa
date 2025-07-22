from typing import Optional

from .node import Node


def how_high(root: Optional[Node]) -> int:
    if root is None:
        return -1

    left_count = how_high(root.left)
    right_count = how_high(root.right)

    return 1 + max(left_count, right_count)


# Time complexity: O(n)
# Space complexity: O(n)
