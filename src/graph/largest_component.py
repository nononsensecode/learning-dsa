from typing import Dict, List


def largest_component(graph: Dict[str, List[str]]) -> int:
    visited = set[str]()
    largest = 0
    for node in graph:
        length = _explore(graph, visited, node)
        if length > largest:
            largest = length

    return largest


def _explore(graph: Dict[str, List[str]], visited: set[str], node: str) -> int:
    if node in visited:
        return 0

    visited.add(node)

    count = 1
    for neighbour in graph[node]:
        if neighbour not in visited:
            count += _explore(graph, visited, neighbour)

    return count

# "e" is the number of edges
# "n" is the number of nodes
# Time complexity: O(e)
# Space complexity: O(n)