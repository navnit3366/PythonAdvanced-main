import re
string = input()
food_storage = []
pattern = r"(?P<symbol>(\||#))(?P<item>[A-Za-z ]+)(?P=symbol)(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})(?P=symbol)(?P<calories>\d+)(?P=symbol)"
sum_of_calories = 0
result = [obj.groupdict() for obj in re.finditer(pattern, string)]

for dictionary in result:
    food_storage.append([dictionary["item"],dictionary["date"],int(dictionary["calories"])])
    sum_of_calories += int(dictionary["calories"])

# print(food_storage)
days_to_last = sum_of_calories // 2000
print(f"You have food to last you for: {days_to_last} days!")

for item in food_storage:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")
