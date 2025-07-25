from typing import List


def five_sort(nums: List[int]) -> List[int]:
    head = 0
    tail = len(nums) - 1

    while head < tail:
        if nums[head] != 5:
            head += 1
            continue

        if nums[tail] == 5:
            tail -= 1
            continue

        temp = nums[tail]
        nums[head] = temp
        nums[tail] = 5
        tail -= 1
        head += 1

    return nums

# Time complexity: O(n)
# Space complexity: O(1)