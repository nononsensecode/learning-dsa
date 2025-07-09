def sum_of_lengths(strings: list[str]) -> int:
    if len(strings) == 0:
        return 0

    return len(strings[0]) + sum_of_lengths(strings[1:])

# Time complexity: O(n^2)
# Space complexity: O(n^2)