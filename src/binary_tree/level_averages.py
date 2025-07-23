from .node import Node
from typing import Optional, List, Tuple
from statistics import mean

def level_averages(root: Optional[Node]) -> List[float]:
    levels = []
    _level_averages((root, 0), levels)

    averages = []
    for level in levels:
        averages.append(mean(level))

    return averages


def _level_averages(current: Tuple[Optional[Node], int], levels: List[List[int]] = []):
    node = current[0]
    level = current[1]

    if not node:
        return
    
    if len(levels) == level:
        levels.append([])

    levels[level].append(node.val)

    if node.left:
        _level_averages((node.left, level+1), levels)

    if node.right:
        _level_averages((node.right, level+1), levels)

def level_averages_iterative(root: Optional[Node]) -> List[float]:
    stack = [(root, 0)]
    levels = []

    while stack:
        current = stack.pop()
        node = current[0]
        level = current[1]
        if not node:
            continue

        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)

        if node.right:
            stack.append((node.right, level+1))

        if node.left:
            stack.append((node.left, level+1))

    averages = []
    for level in levels:
        averages.append(mean(level))

    return averages

    
# Time complexity O(n)
# Space complexity O(n)

