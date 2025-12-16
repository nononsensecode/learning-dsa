from typing import Optional

def max_path_sum(grid: list[list[int]], memo: Optional[dict[tuple[int, int], int|float]] = None, row: int = 0, col: int = 0) -> int|float:
    if memo is None:
        memo = {}

    pos = (row, col)
    if pos in memo:
        return memo[pos]
    
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]
    
    if row >= len(grid) or col >= len(grid[0]):
        return float("-Inf")
    
    right = max_path_sum(grid, memo, row, col + 1)
    down = max_path_sum(grid, memo, row + 1, col)
    total = grid[row][col] + max(right, down)

    memo[pos] = total
    return total

# r = number of rows
# c = number of columns
# Time complexity = O(r*c)
# Space complexity = O(r*c)