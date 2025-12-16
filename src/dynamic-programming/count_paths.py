from typing import Optional

def count_paths(grid: list[list[str]], memo: Optional[dict[str, int]] = None, row: int = 0, col: int = 0) -> int:
    if memo == None:
        memo = {}

    pos = f"{row},{col}"
    if pos in memo:
        return memo[pos]
    
    if row == len(grid) - 1 and col == len(grid[0]) - 1 and grid[row][col] != "X":
        return 1
    
    if row >= len(grid) or col >= len(grid[0]):
        return 0
    
    if grid[row][col] == "X":
        return 0
    
    right = count_paths(grid, memo, row, col + 1)
    down = count_paths(grid, memo, row + 1, col)
    total = right + down

    memo[pos] = total
    return memo[pos]
        
# r = number of rows
# c = number of columns
# Time complexity = O(r*c)
# Space complexity = O(r*c)