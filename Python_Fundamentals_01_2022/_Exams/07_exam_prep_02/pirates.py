def gather_settlements_data():
    settlements_ = {}
    settlement = input()
    # settlements = {}
    while settlement != "Sail":
        settlement_split = settlement.split("||")
        if settlement_split[0] in settlements_:
            settlements_[settlement_split[0]][0] += int(settlement_split[1])
            settlements_[settlement_split[0]][1] += int(settlement_split[2])
        else:
            settlements_[settlement_split[0]] = [int(settlement_split[1]), int(settlement_split[2])]
        settlement = input()
    return settlements_


def pirates_operations():
    command = input()
    while command != "End":
        spl_command = command.split("=>")
        this_command = spl_command[0]
        town = spl_command[1]
        if this_command == "Plunder":
            killed_people = int(spl_command[2])
            gold_plundered = int(spl_command[3])
            settlements[town][0] -= killed_people
            settlements[town][1] -= gold_plundered
            print(f"{town} plundered! {gold_plundered} gold stolen, {killed_people} citizens killed.")
            if settlements[town][0] == 0 or settlements[town][1] == 0:
                del settlements[town]
                print(f"{town} has been wiped off the map!")
        elif this_command == "Prosper":
            before_prosper_gold = settlements[town][1]
            gold_added = int(spl_command[2])
            if gold_added >= 0:
                settlements[town][1] += gold_added
                print(f"{gold_added} gold added to the city treasury. {town} now has {settlements[town][1]} gold.")
            else:
                print(f"Gold added cannot be a negative number!")
        command = input()


def print_pirates_plans(dict_data):
    if len(dict_data) > 0:
        print(f"Ahoy, Captain! There are {len(dict_data)} wealthy settlements to go to:")
        for town, data in dict_data.items():
            print(f"{town} -> Population: {data[0]} citizens, Gold: {data[1]} kg")
    else:
        print(f"Ahoy, Captain! All targets have been plundered and destroyed!")


settlements = gather_settlements_data()
pirates_operations()
print_pirates_plans(settlements)
