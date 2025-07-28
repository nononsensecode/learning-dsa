from typing import Dict, Tuple, List

def undirected_path(edges: List[Tuple[str, str]], node_A: str, node_B: str) -> bool:
    graph = _create_adj_list(edges)
    stack = [node_A]
    visited = set()

    while stack:
        current = stack.pop()
        if current == node_B:
            return True
        
        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)

    return False
        


def _create_adj_list(edges: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    adj_list = {}
    for edge in edges:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
        if edge[1] not in adj_list:
            adj_list[edge[1]] = []
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    return adj_list


# e is number of edges
# n is number of nodes
# Time complexity: O(e)
# Space complexity: O(e)