from typing import Dict, List


def longest_path(graph: Dict[str, List[str]]) -> int:
    distances = {}
    for node in graph:
        if len(graph[node]) == 0:
            distances[node] = 0
    
    for node in graph:
        traverse_distances(graph, node, distances)

    return max(distances.values())


def traverse_distances(graph: Dict[str, List[str]], node: str, distances: Dict[str, int]) -> int:
    if node in distances:
        return distances[node]
    
    largest = 0
    for neighbour in graph[node]:
        attempt = traverse_distances(graph, neighbour, distances)
        if attempt > largest:
            largest = attempt

    distances[node] = 1 + largest
    return distances[node]

