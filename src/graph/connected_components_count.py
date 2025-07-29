from typing import Dict, List


def connected_components_count(graph: Dict[str, List[str]]) -> int:
    visited = set[str]()
    count = 0
    for node in graph:
        count += 1 if _explore_recursive(graph, visited, node) else 0

    return count


def _explore(graph: Dict[str, List[str]], visited: set[str], node: str) -> bool:
    if node in visited:
        return False

    stack = [node]
    while stack:
        current = stack.pop()
        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)

    return True


def _explore_recursive(
    graph: Dict[str, List[str]], visited: set[str], node: str
) -> bool:
    if node in visited:
        return False

    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            _explore_recursive(graph, visited, neighbour)

    return True

# "e" is number of edges
# "n" is number of nodes
# Time complexity: O(e)
# Space complexity: O(n)