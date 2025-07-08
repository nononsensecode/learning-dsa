def longest_word(sentence: str) -> str:
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(longest) <= len(word):
            longest = word

    return longest
