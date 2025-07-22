from typing import Optional

from .node import Node


def tree_value_count(root: Optional[Node], target: str) -> int:
    if root is None:
        return 0

    left_count = tree_value_count(root.left, target)
    right_count = tree_value_count(root.right, target)

    count = 1 if root.val == target else 0
    return count + left_count + right_count
