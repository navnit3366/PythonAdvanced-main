import re
text = input()
search_word = input()
# pattern = rf"{search_word}(?=[\s.,\?\!:])"
pattern = rf"\b{search_word}\b"

result = re.findall(pattern, text, re.IGNORECASE)
print(len(result))