travel = input()
command = input()
while command != "Travel":
    s_command = command.split(":")
    c_command = s_command[0]
    if c_command == "Add Stop":
        c_index = int(s_command[1])
        c_string = s_command[2]
        if c_index <= len(travel):
            part_a = travel[:c_index]
            part_b = travel[c_index:]
            travel = part_a + c_string + part_b
            print(travel)
    elif c_command == "Remove Stop":
        c_start_index = int(s_command[1])
        c_end_index = int(s_command[2])
        if c_end_index >= 0 or c_start_index >0 :
            travel = travel[:c_start_index] + travel[c_end_index+1:]
            print(travel)

    elif c_command == "Switch":
        c_old_string = s_command[1]
        c_new_string = s_command[2]
        travel = travel.replace(c_old_string, c_new_string)
        print(travel)
    command = input()
print(f"Ready for world tour! Planned stops: {travel}")