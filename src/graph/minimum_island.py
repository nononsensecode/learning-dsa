from typing import List, Set, Tuple


def minimum_island(grid: List[List[str]]) -> float:
    visited: Set[Tuple[int, int]] = set()
    smallest = float("inf")

    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            size = _explore(grid, row_index, col_index, visited)
            if size > 0 and size < smallest:
                smallest = size

    return smallest


def _explore(
    grid: List[List[str]],
    row_index: int,
    col_index: int,
    visited: Set[Tuple[int, int]],
) -> int:
    row_inbound = 0 <= row_index < len(grid)
    col_inboud = 0 <= col_index < len(grid[0])
    if not row_inbound or not col_inboud:
        return 0

    if grid[row_index][col_index] == "W":
        return 0

    pair: Tuple[int, int] = (row_index, col_index)
    if pair in visited:
        return 0

    visited.add(pair)

    size = 1
    size += _explore(grid, row_index - 1, col_index, visited)
    size += _explore(grid, row_index + 1, col_index, visited)
    size += _explore(grid, row_index, col_index - 1, visited)
    size += _explore(grid, row_index, col_index + 1, visited)

    return size


# m is the number of rows and n is the number of columns
# Time complexity: O(m*n)
# Space complexity: O(m*n)
