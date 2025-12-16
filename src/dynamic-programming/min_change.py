from typing import Optional


def min_change(
    amount: int, coins: list[int], memo: Optional[dict[int, int]] = None
) -> int:
    if memo is None:
        memo = {}

    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0

    counts = []
    for coin in coins:
        if coin > amount:
            continue

        count = min_change(amount - coin, coins, memo)
        if count < 0:
            continue
        counts.append(count)

    minimum = -1
    if len(counts) > 0:
        minimum = min(counts) + 1

    memo[amount] = minimum
    return minimum


min_change(23, [2, 5, 7])

# a = amount
# c = count of coins
# Time complexity = O(a*c)
# Space complexity = O(a) (suppose coin is 1)
