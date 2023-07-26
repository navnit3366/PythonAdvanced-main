import re


def planet_print(list_of_planets):
    if len(list_of_planets) > 0:
        for planet in list_of_planets:
            print(f"-> {planet}")


data_count = int(input())
attacked_planets = []
destroyed_planets = []

for line in range(data_count):
    current_line = input()
    counter = 0
    counter += current_line.lower().count("s")
    counter += current_line.lower().count("t")
    counter += current_line.lower().count("a")
    counter += current_line.lower().count("r")
    decoded_text = ""
    for idx in range(len(current_line)):
        new_char = chr((ord(current_line[idx]) - counter))
        decoded_text += new_char
    # pattern = r"@(?P<name>[A-Za-z]+)(([0-9]+?)|:)((\:|)(?P<population>\d+))(\!)(?P<a_type>[AD])(\!)(\-\>)(?P<s_count>\d+)"
    pattern = r"@(?P<name>[A-Za-z]+)(([0-9]+?)|:)((\:|)(?P<population>\d+))(\!)(?P<a_type>[AD])(\!)(\-\>)(?P<s_count>\d+)"
    result = [word.groupdict() for word in re.finditer(pattern, decoded_text)]
    if len(result) > 0:
        if result[0]["a_type"] == "A":
            attacked_planets.append(result[0]["name"])
        else:
            destroyed_planets.append(result[0]["name"])
print(f"Attacked planets: {len(attacked_planets)}")
planet_print(attacked_planets)
print(f"Destroyed planets: {len(destroyed_planets)}")
planet_print(destroyed_planets)