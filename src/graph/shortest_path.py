from collections import deque
from typing import Dict, List


def shortest_path(edges: List[List[str]], node_A: str, node_B: str) -> int:
    adj_list: Dict[str, List[str]] = _convert_to_adj_list(edges)
    queue = deque([(node_A, 0)])
    visited = set[str]()

    while queue:
        current = queue.popleft()
        node, count = current
        if node in visited:
            continue

        if node == node_B:
            return count
        visited.add(node)

        for neighbour in adj_list[node]:
            if neighbour not in visited:
                queue.append((neighbour, count + 1))

    return -1


def _convert_to_adj_list(edges: List[List[str]]) -> Dict[str, List[str]]:
    adj_list = {}

    for edge in edges:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
        if edge[1] not in adj_list:
            adj_list[edge[1]] = []

        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    return adj_list


# "e" is the number of edges
# "n" is the number of nodes
# Time complexity: O(e)
# Space complexity: O(n)
