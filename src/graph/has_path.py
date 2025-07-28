from typing import Dict, List
from collections import deque


def has_path(graph: Dict[str, List[str]], src: str, dst: str) -> bool:
    stack = [src]

    while stack:
        current = stack.pop()
        if current == dst:
            return True

        for neighbour in graph[current]:
            stack.append(neighbour)

    return False

def has_path_bread_first(graph: Dict[str, List[str]], src: str, dst: str) -> bool:
    queue = deque([src])

    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)

    return False

def has_path_recursive(graph: Dict[str, List[str]], src: str, dst: str) -> bool:
    if src == dst:
        return True 

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst):
            return True
        
    return False

# "n" is number of nodes and "e" is number of edges
# Time complexity: O(e)
# Space complexity: O(n)