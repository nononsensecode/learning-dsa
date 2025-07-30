from collections import deque
from typing import List, Set, Tuple


def closest_carrot(grid: List[List[str]], starting_row: int, starting_col: int) -> int:
    visited: Set[Tuple[int, int]] = set()

    queue = deque([(starting_row, starting_col, 0)])
    while queue:
        current_pos = queue.popleft()
        row, col, count = current_pos
        if (row, col) in visited:
            continue

        row_inbound = 0 <= row < len(grid)
        col_inbound = 0 <= col < len(grid[0])
        if not row_inbound or not col_inbound:
            continue

        visited.add((row, col))
        if grid[row][col] == "X":
            continue

        if grid[row][col] == "C":
            return count

        queue.append((row + 1, col, count + 1))
        queue.append((row - 1, col, count + 1))
        queue.append((row, col + 1, count + 1))
        queue.append((row, col - 1, count + 1))

    return -1

# "m" is the number of rows
# "n" is the number columns
# Time complexity: O(m*n)
# Space complexity: O(m*n)
