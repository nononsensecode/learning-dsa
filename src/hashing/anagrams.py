from typing import Dict
from collections import Counter

def anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)

# def anagrams(s1: str, s2: str) -> bool:
#     if len(s1) != len(s2):
#         return False
#
#     s1_counter = _letter_count(s1)
#     s2_counter = _letter_count(s2)
#
#     for s, count in s1_counter.items():
#         if s not in s2_counter:
#             return False
#
#         if s2_counter[s] != count:
#             return False
#
#
#     return True

def _letter_count(word: str) -> Dict[str, int]:
    letters: Dict[str, int] = {}
    for letter in word:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    return letters

# Time complexity = O(m+n)
# Space complexity = O(m+n)