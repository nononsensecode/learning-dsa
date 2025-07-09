def pair_sum(numbers: list[int], target: int) -> tuple[int, int]:
    previous_nums = {}
    result: tuple[int, int] = (-1, -1)

    for num_index, num in enumerate(numbers):
        compliment = target - num
        if compliment in previous_nums:
            result = (previous_nums[compliment], num_index)
            break

        previous_nums[num] = num_index

    return result

# Time complexity = O(n)
# Space complexity = O(n)

# def pair_sum(numbers: list[int], target: int) -> tuple[int, int]:
#     result: tuple[int, int] = (0, 0)
#     for i in range(0, len(numbers)):
#         for j in range (i+1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 result = (i, j)
#                 break
#
#     return result


