from typing import Tuple, Dict, List


def semesters_required(num_courses: int, prereqs: List[Tuple[int, int]]) -> int:
    graph = _create_graph(prereqs)
    distances = _ending_points_with_distance(graph)
    if not len(distances.values()):
        return 1

    for course in range(num_courses):
        _traverse(graph, course, distances)

    return max(distances.values())


def _create_graph(prereqs: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    graph: Dict[int, List[int]] = {}
    for item in prereqs:
        prereq, course_id = item
        if prereq not in graph:
            graph[prereq] = []
        if course_id not in graph:
            graph[course_id] = []
        graph[prereq].append(course_id)

    return graph


def _ending_points_with_distance(graph: Dict[int, List[int]]) -> Dict[int, int]:
    distances: Dict[int, int] = {}
    for node in graph:
        if len(graph[node]) == 0:
            distances[node] = 1

    return distances


def _traverse(graph: Dict[int, List[int]], node: int, distances: Dict[int, int]) -> int:
    if node in distances:
        return distances[node]

    longest_distance = 0
    for neighbour in graph[node]:
        distance = _traverse(graph, neighbour, distances)
        if distance > longest_distance:
            longest_distance = distance

    distances[node] = 1 + longest_distance
    return distances[node]
