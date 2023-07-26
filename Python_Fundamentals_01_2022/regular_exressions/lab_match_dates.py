import re
text = input()
pattern = r"\d{2}([\.\-\/])[A-Z][a-z]{2}\1\d{4}\b"
match = [obj.groupdict() for obj in re.finditer(pattern, text)]
for k in match:
    print(f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}")