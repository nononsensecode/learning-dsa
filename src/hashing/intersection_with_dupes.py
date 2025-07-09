from collections import Counter

def intersection_with_dupes(a: list[str], b: list[str]) -> list[str]:
    a_counter = Counter(a)
    b_counter = Counter(b)
    result = []

    for item_a, count_a in a_counter.items():
        if item_a in b_counter:
            for _ in range(0, min(count_a, b_counter[item_a])):
                result.append(item_a)

    return result

# Time Complexity: O(2n+m) = O(n+m)
# Space Complexity: O(n+m)