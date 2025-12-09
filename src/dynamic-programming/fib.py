def fib(n: int, memo: dict[int, int] = {}) -> int:
    if n == 0 or n == 1:
        return n

    if n in memo:
        return memo[n]

    f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return memo[n]


if __name__ == "__main__":
    print(fib(46))

# without memoization
"""
                            fib(5)
                          /        \
                    fib(4)            fib(3)
                   /      \           /      \
              fib(3)      fib(2)   fib(2)   fib(1)
              /    \      /    \   /    \     
          fib(2) fib(1) fib(1) fib(0) fib(1) 
          /   \    
      fib(1) fib(0)

      Time complexity = O(2^n)
      Space complexity = O(n)
"""
# with memoization
"""
                 fib(5)
               /        \
          fib(4)         fib(3) ⚡ cache hit
         /      \        
     fib(3)   fib(2) ⚡ cache hit
     /   \     
  fib(2) fib(1)
  /   \
fib(1) fib(0)
"""
# Time complexity without memoization: O(2^n)
# Time complexity with memoization: O(n)
# Space complexity with and without memoization: O(n)
