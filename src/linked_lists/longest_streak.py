from typing import Optional

from .node import Node


def longest_streak(n: Node) -> int:
    if n is None:
        return 0

    current = n.next
    prev_val = n.val
    streak = 1
    longest = 1

    while current is not None:
        if prev_val == current.val:
            streak += 1
        else:
            streak = 1
            prev_val = current.val

        if longest < streak:
            longest = streak
        current = current.next

    return longest


# Time Complexity: O(n)
# Space Complexity: O(1)
