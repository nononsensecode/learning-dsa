from typing import Optional

from src.binary_tree.node import Node


def max_path_sum(root: Optional[Node]) -> float:
    print(f"Placed the function with {root.val if root else "None"} to the stack")
    if root is None:
        return float("-inf")

    if root.left is None and root.right is None:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


#    /    \
#   11     4
#  / \      \
# 4   -2     1
"""
1. check whether 3 is None
2. check whether the left and right of 3 is None
3. 3 + max(max_path_sum(11), max_path_sum(4))
4. placed max_path_sum(11) in to the stack
5. check whether 11 is None
6. check whether left and right of 11 is None
7. 11 + max(max_path_sum(4), max_path_sum(-2))
8. place max_path_sum(4) to stack
9. check whether 4 is None
10. check whether left and right of 4 is None. As it is true, return 4
11. 11 + max(4, max_path_sum(-2))
12. placed max_path_sum(-2) to the stack
13. check whether -2 is None
14. check whether left and right of -2 is None.As it is true, return -2
15. 11 + max(4, -2) = 11 + 4 = 15
16. 3 + max(15, max_path_sum(4))
17. check whether 4 is None
18. Check whether left and right of 4 is None
19. 4 + max(max_path_sum(None), max_path_sum(1))
20. Placeced max_path_sum(None) to the stack
21. As it is None, return float("-inf)
22 4 + max(float("-inf"), max_path_sum(1))
23. placed max_path_sum(1) to the stack
24. Check whether 1 is None
25. Check whether left and right is None. As it is True return 1
26. 4 + max(float("-inf"), 1) = 4 + 1 = 5
27. 3 + max(15, 5) = 3 + 15 = 18

"""

# Time Complexity: O(n)
# Space Complexity: O(n)
