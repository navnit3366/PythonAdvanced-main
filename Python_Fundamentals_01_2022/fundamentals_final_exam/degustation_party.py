unsplit_command = input()
guests = {}

while unsplit_command != "Stop":
    split_data = unsplit_command.split("-")
    command = split_data[0]
    guest = split_data[1]
    meal = split_data[2]
    if command == "Like":
        if guest in guests:
            if meal not in guests[guest]:
                guests[guest][meal] = "like"
        else:
            guests[guest] = {meal:"like"}
    elif command == "Dislike":
        if guest in guests:
            if meal in guests[guest] and guests[guest][meal] == "like":
                guests[guest][meal] = "dislike"
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")
    unsplit_command = input()
# print(guests)
disliked = 0
for guest, data in guests.items():
    meals = []
    for meal, opinion in data.items():
        if opinion == "dislike":
            disliked += 1
        else:
            meals.append(meal)
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {disliked}")

