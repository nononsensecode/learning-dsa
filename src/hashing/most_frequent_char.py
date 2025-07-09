from collections import Counter

def most_frequent_char(string: str) -> str:
    counter = Counter(string)

    most_frequent = string[0]
    for s in string:
        if counter[s] > counter[most_frequent]:
            most_frequent = s

    return most_frequent

# Time complexity = O(2n) = O(n)
# Space complexity = O(n)