from typing import List, Tuple, Set

def island_count(grid: List[List[str]]) -> int:
    visited: Set[Tuple[int, int]] = set()
    count = 0
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if _explore(grid, row_index, col_index, visited):
                count += 1
    return count

def _explore(grid: List[List[str]], row_index: int, col_index: int, visited: Set[Tuple[int, int]]) -> bool:
    row_inbounds = 0 <= row_index < len(grid)
    col_inbounds = 0 <= col_index < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False
    
    if grid[row_index][col_index] == "W":
        return False
    
    pos = (row_index, col_index)
    if pos in visited:
        return False
    
    visited.add(pos)

    # below is only to add "L" to visited set
    _explore(grid, row_index-1, col_index, visited)
    _explore(grid, row_index+1, col_index, visited)
    _explore(grid, row_index, col_index+1, visited)
    _explore(grid, row_index, col_index-1, visited)

    # we will be returning True only if there is atleast a single "L", that is not visited
    return True
    
# Let m is number of rows and n is number of columns
# As we are using nested loops to traverse the grid
# Time complexity: O(m*n)
# Space complexity: O(m*n) as we have to add elements to set (worst case scenario: single island contains the whole grid)

