from typing import Any, Optional


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
