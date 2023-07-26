import re
string = input()
destinations = []
travel_points = 0
pattern = r"(?P<symbol>(=|/))(?P<place>[A-Z][A-Za-z]{2,})(?P=symbol)"

# result = [obj.groupdict() for obj in re.finditer(pattern, string)]
result = re.finditer(pattern, string)

for match_object in result:
    place = match_object["place"]  # ! взима имената на групите създадени в регекс - "place" е име на regex групата дефиниранa в regex патерна по-горе !
    destinations.append(place)
    travel_points += len(place)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")