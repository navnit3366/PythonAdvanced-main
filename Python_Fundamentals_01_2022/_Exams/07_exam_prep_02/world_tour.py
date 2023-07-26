stops = input()
command = input()
while command != "Travel":
    current_command = command.split(":")
    this_command = current_command[0]
    if this_command == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]
        if 0 <= index <= len(stops):
            stops = stops[:index] + string + stops[index:]
    elif this_command == "Remove Stop":
        s_index = int(current_command[1])
        e_index = int(current_command[2])
        if 0 <= s_index <= e_index <= len(stops):
            stops = stops[:s_index] + stops[e_index+1:]
    elif this_command == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
