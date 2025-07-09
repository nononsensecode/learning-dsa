def sum_numbers_recursive(numbers) -> int:
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])

# Time Complexity: O(n^2) As we have to slice the array. n times we have to slice it
# Space Complexity: O(n^2) Same here