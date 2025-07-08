from math import floor, sqrt


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    # factors come in pairs. so if you take square root of the number
    # and range up to that will be sufficient, excluding 1 (1 and the
    # number itself is already a factor)
    for factor in range(2, floor(sqrt(n)) + 1):
        if n % factor == 0:
            return False

    return True


"""
Time complexity = O(sqrt(n))
Space complexit = O(1)
"""
