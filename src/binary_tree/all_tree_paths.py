from typing import Any, List, Optional

from .node import Node


def all_tree_paths(root: Optional[Node]) -> List[List[Any]]:
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    left_paths = all_tree_paths(root.left)
    right_paths = all_tree_paths(root.right)

    if left_paths:
        for p in left_paths:
            p.insert(0, root.val)

    if right_paths:
        for p in right_paths:
            p.insert(0, root.val)

    return [*left_paths, *right_paths]

#      a
#    /   \
#   b     c
#  / \    / \
# d   e  f   g
"""
In the above diagram, you can see that the number of nodes in this balanced tree:

Nodes = 7
Leaves = 4
Balance (Other nodes)  = 3
"""
#          a
#        /   \
#       b     c
#      / \    / \
#     d   e  f   g
#   / \  / \ / \ / \
#  h  i j  k l m n o
"""
In the above diagram:
Nodes = 15
Leaves = 8
Other nodes = 7

So there is a relationship between "Other nodes" and "leaves", and that is:
Other Nodes = Leaves - 1
Total number of nodes = Other Nodes + Leaves = Leaves + Leaves - 1 = 2 * (Leaves) - 1
As 1 is a constant, we can ignore it.

So total nodes = 2 * (Leaves), or in another way:

Number of leaves (l) = Number of nodes/2 or n/2

There is a relationship we can derive from the height(h) and number of nodes(n) also:
n = 2^h - 1

we can ignore the constant 1, so:
n = 2^h

We can write it in logarithmic way as follows:
log(n) = h

So we have the following:
nodes = n
height = log(n)
leaves = n/2

time complexity = O(number of leaves * height) = O(n/2 * log(n)) = O(n * log(n))
space complexity = O(n * log(n))
"""

