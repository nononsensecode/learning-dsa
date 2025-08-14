from typing import Dict, List


def longest_path(graph: Dict[str, List[str]]) -> int:
    distances: Dict[str, int] = _find_end_points_with_distance(graph)
    for node in graph:
        _traverse(graph, node, distances)

    return max(distances.values())


def _find_end_points_with_distance(graph: Dict[str, List[str]]) -> Dict[str, int]:
    ending_points: Dict[str, int] = {}
    for node in graph:
        if len(graph[node]) == 0:
            ending_points[node] = 0

    return ending_points


def _traverse(graph: Dict[str, List[str]], node: str, distances: Dict[str, int]) -> int:
    if node in distances:
        return distances[node]

    largest_distance = 0
    for neighbour in graph[node]:
        distance = _traverse(graph, neighbour, distances)
        if distance > largest_distance:
            largest_distance = distance

    distances[node] = 1 + largest_distance
    return distances[node]
