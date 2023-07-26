import re
string = input()
# pattern = r"(?P<symbol>(=|\/))(?P<country>[A-Z][A-Za-z]+)(?P=symbol)"
pattern = r"(?P<symbol>(=|\/))(?P<country>[A-Z][A-Za-z]{2,})(?P=symbol)"
countries = []
travel_points = 0
result = [obj.groupdict() for obj in re.finditer(pattern, string)]
for dict in result:
    countries.append(dict["country"])
    travel_points += len(dict["country"])
print(f"Destinations: {', '.join(countries)}")
print(f"Travel Points: {travel_points}")