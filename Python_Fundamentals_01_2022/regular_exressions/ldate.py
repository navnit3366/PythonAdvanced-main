import re

text = input()

pattern = r"(?P<D>\d{2})([\.\-\/])(?P<M>[A-Z][a-z]{2})\2(?P<Y>\d{4}\b)"

# valid_dates = re.findall(pattern, text)
# print(valid_dates)

valid_dates = [m_obj.groupdict() for m_obj in re.finditer(pattern, text)]
# for date in valid_dates:
for date in valid_dates:
    print(f"Day: {date['D']}, Month: {date['M']}, Year: {date['Y']}")
