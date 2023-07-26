import re
text = input()
pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\.\-\_]?[A-Za-z0-9]+@[A-Za-z]+-?[A-Za-z]+(\.[A-Za-z]+)+"
result = [obj.group() for obj in re.finditer(pattern, text)]
print(*result , sep="\n")