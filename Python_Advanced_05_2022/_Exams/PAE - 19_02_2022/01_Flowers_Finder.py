from collections import deque


def found_vowels_and_consonants(search_words, vowel_char, consonant_char):
    # function that found vowel or consonant in list of search_words
    chars = set()
    for word in searched_words:
        if vowels_char in word:
            found_chars.add(vowel_char)
        if consonants_char in word:
            found_chars.add(consonant_char)
    return chars


def all_chars_in_word_check(list_of_search_words, f_chars):
    # function that check does f_chars are enough to form a word from a list_of_search_words
    for i in range(len(list_of_search_words)):
        check_word = list_of_search_words[i]
        for char in f_chars:
            check_word = check_word.replace(char, "")
            if not check_word:
                return list_of_search_words[i]


vowels = deque(input().split(" "))
consonants = input().split(" ")
searched_words = [
    "rose",
    "tulip",
    "lotus",
    "daffodil",
    ]
found_chars = set()
found_word = ""

while True:
    vowels_char = vowels.popleft()
    consonants_char = consonants.pop()
    found_chars.update(found_vowels_and_consonants(searched_words, vowels_char, consonants_char))
    found_word = all_chars_in_word_check(searched_words, found_chars)

    if found_word:
        break

    if (not vowels) or (not consonants):
        break

if found_word:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
