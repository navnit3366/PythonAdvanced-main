import re
racers = input().split(", ")
racing_data = {}
data = input()
while data != "end of race":
    name_pattern = r"([A-Za-z])"
    distance_pattern = r"(\d)"

    name = re.findall(name_pattern, data)
    distance = [int(element) for element in re.findall(distance_pattern, data)]

    distance = sum(distance)
    name = ("".join(name))

    if name in racers:
        if name in racing_data:
            racing_data[name] += distance
        else:
            racing_data[name] = distance
            
    data = input()

sorted_racers_list = list({k: v for k, v in sorted(racing_data.items(), key=lambda item: item[1], reverse=True)})
print(f"1st place: {sorted_racers_list[0]}")
print(f"2nd place: {sorted_racers_list[1]}")
print(f"3rd place: {sorted_racers_list[2]}")