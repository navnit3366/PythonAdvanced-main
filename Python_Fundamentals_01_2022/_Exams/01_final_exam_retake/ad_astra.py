import re

input_string = input()
data = {}
calories_sum = 0
pattern = r"(?P<symbol>(#|\|))(?P<food>[A-Za-z ]+)(?P=symbol)(?P<date>\d{2}/\d{2}/\d{2})(?P=symbol)(?P<callories>\d+)(?P=symbol)"

result = [obj.groupdict() for obj in re.finditer(pattern, input_string)]
# print(result)
if len(result) > 0:
    for element in result:
        if 0 <= int(element["callories"]) <= 10000:
            data[element["food"]] = [element["date"],int(element["callories"])]
            calories_sum += int(element["callories"])
# print(data)
print(f"You have food to last you for: {calories_sum//2000} days!")
if len(result) > 0:
    for item, d_cal in data.items():
        print(f"Item: {item}, Best before: {d_cal[0]}, Nutrition: {d_cal[1]}")