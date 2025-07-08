def max_value(nums: list[int]) -> int:
    m = -1
    for num in nums:
        if m < num:
            m = num
    return m
