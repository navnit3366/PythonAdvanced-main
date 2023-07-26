number_of_initial_plants = int(input())
plants_data = {}
for plant in range(number_of_initial_plants):
    c_plant = input().split("<->")
    plants_data[c_plant[0]] = [int(c_plant[1])]
command = input()
while command != "Exhibition":
    split_command = command.split(": ")
    current_command = split_command[0]
    if current_command == "Rate":
        sub_split_command = split_command[1].split(" - ")
        c_plant = sub_split_command[0]
        c_rate = int(sub_split_command[1])
        if c_plant in plants_data:
            plants_data[c_plant].append(c_rate)
        else:
            print(f"error")
    elif current_command == "Update":
        sub_split_command = split_command[1].split(" - ")
        c_plant = sub_split_command[0]
        c_rarity = int(sub_split_command[1])
        if c_plant in plants_data:
            plants_data[c_plant][0] = c_rarity
        else:
            print(f"error")
    elif current_command == "Reset":
        c_plant = split_command[1]
        if c_plant in plants_data:
            plants_data[c_plant]= plants_data[c_plant][:1]
        else:
            print(f"error")
    command = input()

print(f"Plants for the exhibition:")
for plant, data in plants_data.items():
    if (sum(data) - data[0]) > 0:
        average_rating = (sum(data) - data[0]) / (len(data) - 1)
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {data[0]}; Rating: {average_rating:.2f}")
