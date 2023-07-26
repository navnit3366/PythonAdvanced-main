import re
text = input()
pattern = r"(\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b)"
# match = [obj.group() for obj in re.finditer(pattern, text)]
# print(", ".join(match))
match = re.findall(pattern, text)
print(", ".join(match))