city = input()
targets = {}
while city != "Sail":
    c_data = city.split("||")
    town = c_data[0]
    population = int(c_data[1])
    gold = int(c_data[2])
    if town not in targets:
        targets[town] = [population, gold]
    else:
        targets[town][0] += population
        targets[town][1] += gold
    city = input()
command = input()
while command != "End":
    s_command = command.split("=>")
    current_command = s_command[0]
    if current_command == "Plunder":
        c_city = s_command[1]
        c_people = int(s_command[2])
        c_gold = int(s_command[3])
        print(f"{c_city} plundered! {c_gold} gold stolen, {c_people} citizens killed.")
        targets[c_city][0] -= c_people
        targets[c_city][1] -= c_gold
        if targets[c_city][0] <= 0 or targets[c_city][1] <= 0:
            del targets[c_city]
            print(f"{c_city} has been wiped off the map!")
    elif current_command == "Prosper":
        c_city = s_command[1]
        c_gold = int(s_command[2])
        if c_gold >= 0:
            targets[c_city][1] += c_gold
            print(f"{c_gold} gold added to the city treasury. {c_city} now has {targets[c_city][1]} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    command = input()
if len(targets) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for town, data in targets.items():
        print(f"{town} -> Population: {data[0]} citizens, Gold: {data[1]} kg")