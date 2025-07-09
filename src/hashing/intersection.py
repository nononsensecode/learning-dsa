def intersection(a: list[int], b: list[int]) -> list[int]:
    a_members_set = set(a)
    return [element for element in b if element in a_members_set]

# Time Complexity: O(n+m)
# Space Complexity: O(n)

# def intersection(a: list[int], b: list[int]) -> list[int]:
#     char_map = _create_character_map(a)
#     inter: list[int] = []
#     for elem in b:
#         if elem in char_map:
#             inter.append(elem)
#
#     return inter
#
#
# def _create_character_map(a: list[int]) -> dict[int, bool]:
#     m = {}
#     for elem in a:
#         m[elem] = True
#
#     return m