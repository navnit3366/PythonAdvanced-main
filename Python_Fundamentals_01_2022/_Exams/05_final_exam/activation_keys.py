raw_str = input()
command = input()
while command != "Generate":
    s_command = command.split(">>>")
    this_command = s_command[0]
    if this_command == "Contains":
        substring = s_command[1]
        if substring in raw_str:
            print(f"{raw_str} contains {substring}")
        else:
            print(f"Substring not found!")
    elif this_command == "Flip":
        new_case = s_command[1]
        start_index = int(s_command[2])
        end_index = int(s_command[3])
        substring = raw_str[start_index:end_index]
        if new_case == "Lower":
            new_substring = substring.lower()
        else:
            new_substring = substring.upper()
        raw_str = raw_str[:start_index] + new_substring + raw_str[end_index:]
        print(raw_str)
    elif this_command == "Slice":
        s_indx = int(s_command[1])
        e_indx = int(s_command[2])
        raw_str = raw_str[:s_indx] + raw_str[e_indx:]
        print(raw_str)
    command = input()
print(f"Your activation key is: {raw_str}")