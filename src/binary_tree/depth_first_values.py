from typing import List, Optional

from .node import Node


def depth_first_values(root: Optional[Node]) -> List[str]:
    stack = [root]
    result = []

    while stack:
        current = stack.pop()
        if not current:
            continue

        result.append(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result


def depth_first_values_recursive(root: Optional[Node]) -> List[str]:
    if root is None:
        return []

    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)

    return [root.val, *left_values, *right_values]


"""
We have two extreme situations

- Best case scenario: A balanced tree, where both legs of the root is balanced. In that case,
  the relation between the number of nodes (n) and height (h) of the binary tree is:

  n = 2^(h+1) -1
  
  Which can be written also as: 

  h = log_2(n+1)-1

- Worst case scenario: A linked list where the number of nodes equal to the height of the tree.
  i.e, n = h  

 So we need to take the worst situation when calculating time and space complexity. The spread/unpack
 is not a free operation. It must iterate through every element in the `left_values` and `right_values`
 to copy them in to the new list being created.

 - consider a tree where each node has only a left child.
 - The call for the root (with `n` nodes) must copy the `n-1` values from its child's list
 - Its child (with `n-1` nodes) must copy the `n-2` values from its child's list
 - ...and so on.

 The total work is the sum of these copy operations:
 
 T(n) = approx(n-1) + (n-2) + (n-3)+....+1
 
 This is an arithmetic series that sums to:

 n/(n-1)^2 which give a time complexity of O(n^2)

### Space complexity

- In the case of looped solution, we creating a list which is equal to the number
  of nodes. So the space complexity is O(n)
- In the case of recursive solution, we are creating a list also there is function stack which is
  equal to the height(h) of the tree. So the space complexity is actually O(h+n). But we
  know that h<=n, so we can avoid the lesser variable, then the space complexity becomes: O(n)

### Time complexity
- In the case of looped solution, we are looping through each node, then the time complexity
  is O(n)
- In the case of recursive solution, 

We can reduce the time and space complexity in the case of recursive type solution by introducting
an array
"""


def depth_first_values_recursive_improved(
    root: Optional[Node], result: List[str] = []
) -> list[str]:
    if root is None:
        return []

    result.append(root.val)
    depth_first_values_recursive_improved(root.left, result)
    depth_first_values_recursive_improved(root.right, result)
    return result


#        a
#       / \
#      b   c
#     / \   \
#    d   e   f


"""
Recursive
1. check if root i.e 'a' is None as it is not None:
2. left_values = depth_first_values(a.b)
3. right_values = depth_first_values(a.c)
result = ['a', *['b', 'd', 'e'], *['c', 'f']] = ['a', 'b', 'd', 'e', 'c', 'f']

2: check if root i.e is 'b' is None and as it is not None:
2.1: left_values = depth_first_values(b.d)
2.2: right_values = depth_first_values(b.e)
result = ['b', *[d], *[e]] = ['b', 'd', 'e']

2.1: check if root i.e is 'd' is None, and it is not None:
2.1.1: left_values = depth_first_values(None)
2.1.2: right_values = depth_first_values(None)
result = ['d', *[], *[]] = ['d']

2.2. check if root i.e is 'e' is None, and it is not None:
2.2.1: left_values = depth_first_values(None)
2.2.2: right_values = depth_first_values(None)
result = ['e', *[], *[]] = ['e']

2.1.1: return []
2.1.2: return []

2.2.1: return []
2.2.2: return []

3: check if root i.e is 'c' is None and it is not None:
3.1 left_values = depth_first_values(None)
3.2 right_values = depth_first_values(c.f)
result = ['c', *[], *[f]] = ['c', 'f']

3.1 return []

3.2: check if root, i.e, 'f' is None and it is not None: 
3.2.1: left_values = depth_first_values(None)
3.2.2: left_values = depth_first_values(None)
result = ['f', *[], *[]] = ['f']

3.2.1: return []
3.2.2: return []
"""
