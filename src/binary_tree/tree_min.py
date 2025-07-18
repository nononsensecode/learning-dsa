from collections import deque
from typing import Optional

from .node import Node


def tree_min_value(root: Optional[Node]) -> float:
    stack = [root]
    min = root.val if root else -1

    while stack:
        current = stack.pop()
        if not current:
            continue

        if min > current.val:
            min = current.val

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return min


def tree_min_value_breadth_first(root: Optional[Node]) -> float:
    queue = deque[Optional[Node]]([root])
    min = root.val if root else 0

    while queue:
        current = queue.popleft()
        if not current:
            continue

        if min > current.val:
            min = current.val

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return min


def tree_min_value_depth_first_recursive(root: Optional[Node]) -> float:
    if root is None:
        return float("inf")

    smallest_left_value = tree_min_value_depth_first_recursive(root.left)
    smallest_right_value = tree_min_value_depth_first_recursive(root.right)

    return min(root.val, smallest_left_value, smallest_right_value)


# Time complexity for looped solution as well as recursive one is O(n)
# Space complexity for both solutions is also O(n)
