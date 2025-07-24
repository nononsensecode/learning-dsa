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


def compress_two_pointer(s: str) -> str:
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


def compress_recursive(s: str, prev="", count=0, compressed="", index=0) -> str:
    if prev == "":
        prev = s[index]
        s += "*"

    if index == len(s):
        return compressed

    if s[index] == prev:
        count += 1
    else:
        compressed += f"{count if count > 1 else ""}{prev}"
        prev = s[index]
        count = 1
    index += 1

    return compress_recursive(s, prev, count, compressed, index)


# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
    print(compress_recursive("ccaaatsss"))
