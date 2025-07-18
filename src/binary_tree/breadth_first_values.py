from collections import deque
from typing import List, Optional

from .node import Node


def breadth_first_values(root: Optional[Node]) -> List[str]:
    result = []
    queue = deque[Optional[Node]]([root])

    while queue:
        current = queue.popleft()
        if not current:
            continue
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


# Time complexity: O(n)
# Space complexity: O(n)
