from typing import Dict, List
from collections import deque

graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def depth_first_print(graph: Dict[str, List[str]], start: str):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        visited.add(current)
        print(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)


def depth_first_recursive(graph: Dict[str, List[str]], start: str):
    print(start)

    for neighbour in graph[start]:
        depth_first_recursive(graph=graph, start=neighbour)


def breadth_first_print(graph: Dict[str, List[str]], start: str):
    queue = deque([start])

    while queue:
        current = queue.popleft()
        print(current)

        for neighbour in graph[current]:
            queue.append(neighbour)


if __name__ == "__main__":
    depth_first_print(graph=graph, start="a")
    print("*" * 100)
    breadth_first_print(graph=graph, start="a")
    print("*" * 100)
    depth_first_recursive(graph=graph, start="a")
