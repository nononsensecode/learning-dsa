def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    
    return word[0] == word[-1] and is_palindrome(word[1:len(word) - 1])

def is_palindrome_iterative(word: str) -> bool:
    j = len(word) - 1
    for i in range(len(word)):
        if i >= j:
            return True
        if word[i] != word[j]:
            return False
        
        j -= 1            
            
    return True

# Time complexity: O(n)
# Space complexity: O(1) in the case of iterative solution, but in the case of recursive it is O(n)