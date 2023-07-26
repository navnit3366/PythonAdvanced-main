def palindrome(word, index):
    string = word
    if len(word) == 1 or len(word) == 0:
        string += word
        return True
    if word[0] == word[-1]:
        if palindrome(word[1:len(word)-1], index):
            return f"{string} is a palindrome"
        else:
            return f"{string} is not a palindrome"
    return f"{string} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
