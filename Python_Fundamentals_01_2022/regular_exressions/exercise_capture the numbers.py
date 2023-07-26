import re
text = input()
pattern = r"\d+"
numbers = []
while text:
    add_numbers = re.findall(pattern, text)
    numbers.extend(add_numbers)
    text = input()
print(*numbers)