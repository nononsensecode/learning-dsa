def tribonacci(n: int, memo: dict[int, int] = {}) -> int:
    if n in memo:
        return memo[n]

    if n <= 1:
        return 0

    if n == 2:
        return 1

    f = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
    memo[n] = f
    return f


# Without memoization
"""
Level 0:  1 node                                    trib(5)
              ↓                           /            |            |
Level 1:  *3                          trib(4)       trib(3)       trib(2)
              ↓                      /   |   |      /  |  |          |
Level 2:  *3                    trib(3) trib(2) trib(1) trib(2) trib(1) trib(0)
              ↓                 /  |  |    |      |      |       |       |
Level 3:  *3              trib(2) trib(1) trib(0) 1    1    trib(1) trib(0) 1  0
                            |      |       |                  |       |
Level 4:                    1      1       0                  1       0

        n levels deep → O(3^n) time complexity
"""
# With memoization
"""
trib(5) - not in memo, compute
  │
  ├─── trib(4) - not in memo, compute
  │      │
  │      ├─── trib(3) - not in memo, compute
  │      │      │
  │      │      ├─── trib(2) - base case, return 1
  │      │      │
  │      │      ├─── trib(1) - base case, return 1
  │      │      │
  │      │      └─── trib(0) - base case, return 0
  │      │      
  │      │      memo[3] = 2 ✓
  │      │
  │      ├─── trib(2) - base case, return 1
  │      │
  │      └─── trib(1) - base case, return 1
  │      
  │      memo[4] = 4 ✓
  │
  ├─── trib(3) - ⚡ CACHE HIT! return 2 (no recursion)
  │
  └─── trib(2) - base case, return 1
  
  memo[5] = 7 ✓
"""

# Time complexity without memoization O(3^n)
# Time complexity with memoization O(n)
# Space complexity without and with memoization O(n)
