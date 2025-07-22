from collections import deque
from typing import Any, Optional

from .node import Node


def bottom_right_value(root: Optional[Node]) -> Optional[Any]:
    queue = deque([root])
    current = None

    while queue:
        current = queue.popleft()
        if not current:
            continue

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return current.val if current else None

# Time complexity: O(n)
# Space complexity: O(n)