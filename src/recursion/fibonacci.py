def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

# Time Complexity: O(n)
# Space Complexity: O(n)