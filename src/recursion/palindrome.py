def palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True

    return s[0] == s[-1] and palindrome(s[1:-1])

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)