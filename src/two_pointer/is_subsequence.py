def is_subsequence(first: str, second: str) -> bool:
    first_index = 0
    second_index = 0

    if len(first) > len(second):
        return False

    while first_index < len(first) and second_index < len(second):
        if first[first_index] != second[second_index]:
            second_index += 1
            continue

        first_index += 1
        second_index += 1

    return first_index == len(first)


# Let m is the length of the first string
# and n is the length of the second string
# Time complexity: O(n) worst case
# Space complexity: O(1)
