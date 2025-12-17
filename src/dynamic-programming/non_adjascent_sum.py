from typing import Optional


def non_adjascent_sum(
    nums: list[int], memo: Optional[dict[int, int]] = None, index: int = 0
) -> int:
    if memo is None:
        memo = {}

    if index in memo:
        return memo[index]

    if len(nums) == 0:
        return 0

    if len(nums) < index:
        return 0

    first_element = nums[0]

    left = first_element + non_adjascent_sum(nums[2:], memo, index + 2)
    right = non_adjascent_sum(nums[1:], memo, index + 1)

    maximum = max(left, right)
    memo[index] = maximum
    return maximum

def non_adjacent_sum(nums: list[int], memo: Optional[dict[int, int]] = None, index = 0) -> int:
    if memo is None:
        memo = {}

    if index in memo:
        return memo[index]
    
    if index >= len(nums):
        return 0
    
    left = nums[index] + non_adjacent_sum(nums, memo, index + 2)
    right = non_adjacent_sum(nums, memo, index + 1)
    memo[index] = max(left, right)
    return memo[index]

# n = length of nums
# Time complexity = O(n)
# Space complexity = O(n)