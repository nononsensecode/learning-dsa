from .node import Node
from typing import Optional, List

def path_finder(root: Optional[Node], target: str) -> Optional[List[str]]:
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]
    
    left = path_finder(root.left, target)
    right = path_finder(root.right, target)

    if left:
        return [root.val, *left]
    
    if right:
        return [root.val, *right]
    
    return None