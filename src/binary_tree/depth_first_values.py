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


# Time complexity: O(n)
# Space complexity: O(n) as we are adding the values to the list


"""
Recursive
             a
            / \
            b  c
           / \  \
          d   e  f



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
