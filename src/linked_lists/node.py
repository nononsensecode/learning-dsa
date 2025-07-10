from typing import Any, Optional


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next: Optional[Node] = None
