import re
pattern = r"www(\.[A-Za-z0-9-]+)+(\.[A-Za-z]+)+"
text = input()
while text:
    result = [obj.group() for obj in re.finditer(pattern, text)]
    if len(result) > 0:
        print(*result)
    text = input()