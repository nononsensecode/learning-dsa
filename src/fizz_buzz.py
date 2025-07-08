def fizz_buzz(n: int) -> list[str]:
    fizzbuzz = []
    for i in range(1, n + 1):
        divisible_by_3 = i % 3 == 0
        divisible_by_5 = i % 5 == 0
        if divisible_by_3 and divisible_by_5:
            fizzbuzz.append("fizzbuzz")
        elif divisible_by_3:
            fizzbuzz.append("fizz")
        elif divisible_by_5:
            fizzbuzz.append("buzz")
        else:
            fizzbuzz.append(i)
    return fizzbuzz


# Time Complexity = O(n)
# Space Complexity = O(n)
