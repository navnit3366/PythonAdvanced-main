import re

pattern = r"(?<=\s_)(?P<variable>[A-Za-z0-9]+)(?=\s|$)"
text = input()
result = [el.group() for el in re.finditer(pattern, text)]
print (*result, sep=",")