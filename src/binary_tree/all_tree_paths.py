from typing import Any, List, Optional

from .node import Node


def all_tree_paths(root: Optional[Node]) -> List[List[Any]]:
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    left_paths = all_tree_paths(root.left)
    right_paths = all_tree_paths(root.right)

    if left_paths:
        for p in left_paths:
            p.insert(0, root.val)

    if right_paths:
        for p in right_paths:
            p.insert(0, root.val)

    return [*left_paths, *right_paths]

# Time complexity: O(n)
# Space complexity: O(n)