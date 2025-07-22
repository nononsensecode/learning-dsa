from typing import List, Optional, Tuple

from .node import Node


def tree_levels(root: Optional[Node]) -> List[List[str]]:
    stack = [(root, 0)]
    levels = []

    while stack:
        current = stack.pop()
        node: Optional[Node] = current[0]
        level: int = current[1]
        if not node:
            continue

        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)

        if node.right:
            stack.append((node.right, level + 1))

        if node.left:
            stack.append((node.left, level + 1))

    return levels


def tree_levels_recursive(
    root: Optional[Node], levels: List[List[str]] = []
) -> List[List[str]]:
    levels = []
    _tree_levels_recursive((root, 0), levels)
    return levels


def _tree_levels_recursive(
    current: Tuple[Optional[Node], int], levels: List[List[str]] = []
) -> None:
    node = current[0]
    level = current[1]

    if node is None:
        return

    if len(levels) == level:
        levels.append([])

    levels[level].append(node.val)

    _tree_levels_recursive((node.left, level + 1), levels)
    _tree_levels_recursive((node.right, level + 1), levels)


# Time complexity: O(n)
# Space complexity: O(n)
