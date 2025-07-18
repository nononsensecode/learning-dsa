from collections import deque
from typing import Optional

from .node import Node


def tree_sum_depth_vise(root: Optional[Node]) -> int:
    stack = [root]
    sum = 0

    while stack:
        current = stack.pop()
        if not current:
            continue

        sum += current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return sum


def tree_sum_breadth_vise(root: Optional[Node]) -> int:
    queue = deque[Optional[Node]]([root])
    sum = 0

    while queue:
        current = queue.popleft()
        if not current:
            continue

        sum += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return sum


def tree_sum_depth_vise_recursive(root: Optional[Node]) -> int:
    if root is None:
        return 0

    return (
        root.val
        + tree_sum_depth_vise_recursive(root.left)
        + tree_sum_depth_vise_recursive(root.right)
    )


# Time complexity: For both breadth and depth vise looped solutions, it is O(n). In the case of recursive solutions also it O(n)
# Space complexity: It is also O(n) for all solutions
