from typing import Any, Optional


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next: Optional[Node] = None


def assert_equal(a: Optional[Node], b: Optional[Node]) -> bool:
    current_a = a
    current_b = b

    while current_a is not None or current_b is not None:
        if (current_a and current_b) and (current_a.val != current_b.val):
            return False

        current_a = current_a.next if current_a else None
        current_b = current_b.next if current_b else None

    return current_a == None and current_b == None
