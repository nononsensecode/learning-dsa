from typing import Optional


def sum_possible(
    amount: int, numbers: list[int], memo: Optional[dict[int, bool]] = None
) -> bool:
    if memo is None:
        memo = {}

    if amount in memo:
        return memo[amount]

    if amount == 0:
        return True

    is_possible = False
    for num in numbers:
        if num > amount:
            continue
        if sum_possible(amount - num, numbers, memo):
            is_possible = True

    memo[amount] = is_possible
    return is_possible


def sum_possible_another_way(
    amount: int, numbers: list[int], memo: Optional[dict[int, bool]] = None
) -> bool:
    if memo is None:
        memo = {}

    if amount in memo:
        return memo[amount]

    if amount < 0:
        return False

    if amount == 0:
        return True

    for num in numbers:
        if sum_possible_another_way(amount - num, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return False


print(sum_possible(15, [6, 2, 10, 19]))

# a = amount
# n = length of list
# Time complexity = O(a*n)
# Space complexity = O(a)# Space complexity = O(a)
"""
Analysis:

Unique subproblems: Due to memoization, each unique amount value from 0 to the original amount is computed at most once. That gives us O(amount) (consider the list contains 1) unique subproblems.
Work per subproblem: For each subproblem, we iterate through the numbers list, which takes O(n) time.
Total complexity: O(amount) × O(n) = O(amount × n)
"""
