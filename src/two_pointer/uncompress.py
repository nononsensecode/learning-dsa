def uncompress(s: str) -> str:
    uncompressed = ""
    num_as_str = ""
    for i in range(len(s)):
        if s[i].isnumeric():
            num_as_str += s[i]
            continue
        uncompressed += int(num_as_str) * s[i]
        num_as_str = ""

    return uncompressed

def uncompress_two_pointer(s: str) -> str:
    result = []
    i = 0
    j = 0

    while j < len(s):
        if not s[j].isnumeric():
            num = int(s[i:j])
            result.append(s[j] * num)
            i = j + 1

        j += 1

    return "".join(result)

# Number of letters: n
# Max number found: m
# Time complexity: O(n*m)
# Space complexity: O(n*m)