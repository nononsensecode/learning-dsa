def exclusive_items(a: list[int], b: list[int]) -> list[int]:
    a_members = set(a)
    b_members = set(b)

    exclusive = []

    for elem in a:
        if elem not in b_members:
            exclusive.append(elem)

    for elem in b:
        if elem not in a_members:
            exclusive.append(elem)

    return exclusive

# Time Complexity: O(m+n)
# Space Complexity: O(2m+2n) = O(m+n)