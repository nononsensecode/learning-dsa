from .node import Node
from typing import Optional, List, Any

def leaf_list(root: Optional[Node]) -> List[Any]:
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [root.val]

    left_leaves = leaf_list(root.left)
    right_leaves = leaf_list(root.right)

    return [*left_leaves, *right_leaves]

def leaf_list_iterative(root: Optional[Node]) -> List[Any]:
    stack = [root]
    leaves = []

    while stack:
        current = stack.pop()
        if not current:
            continue

        if current.left is None and current.right is None:
            leaves.append(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return leaves

# Time complexity: O(n) for both cases
# Space complexity: O(n) for both cases