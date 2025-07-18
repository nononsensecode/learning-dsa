from collections import deque
from typing import Optional

from .node import Node


def tree_includes_depth_vise(root: Optional[Node], target: str) -> bool:
    stack = [root]

    while stack:
        current = stack.pop()
        if not current:
            continue

        if target == current.val:
            return True

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return False


def tree_includes_breadth_vise(root: Optional[Node], target: str) -> bool:
    queue = deque[Optional[Node]]([root])

    while queue:
        current = queue.popleft()
        if not current:
            continue

        if target == current.val:
            return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False


def tree_includes_depth_vise_recursive(root: Optional[Node], target: str) -> bool:
    if root is None:
        return False

    if target == root.val:
        return True

    return tree_includes_depth_vise_recursive(
        root.left, target
    ) or tree_includes_depth_vise_recursive(root.right, target)


# Time complexity: O(n) for all methods
# Space complexity: O(n) for all methods
