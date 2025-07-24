def compress(s: str) -> str:
    count = 0
    prev = ""
    i = 0
    compressed = ""
    while i < len(s):
        if s[i] != prev and prev != "":
            compressed += f"{count if count > 1 else ""}{prev}"
            count = 0
        prev = s[i]
        count += 1
        i += 1

    compressed += f"{count if count > 1 else ""}{prev}"
    return compressed

def compress_two_pointer(s: str):
    s += "*"
    compressed = ""
    current = 0
    prev = 0
    while current < len(s):
        if s[current] == s[prev]:
            current += 1
        else:
            count = current - prev
            compressed += f"{count if count > 1 else ""}{s[prev]}"
            prev = current

    return compressed


# Time complexity: O(n)
# Space complexity: O(n)