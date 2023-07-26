string = input()
command = input()
while command != "Abracadabra":
    splitted_command = command.split()
    this_command = splitted_command[0]
    if this_command == "Abjuration":
        string = string.upper()
        print(string)
    elif this_command == "Necromancy":
        string = string.lower()
        print(string)
    elif this_command == "Illusion":
        index = int(splitted_command[1])
        letter = splitted_command[2]
        if 0 <= index <= len(string)-1:
            string = string[:index] + letter + string[(index+1):]
            print(f"Done!")
        else:
            print(f"The spell was too weak.")
    elif this_command == "Divination":
        first_s_string = splitted_command[1]
        second_s_string = splitted_command[2]
        if first_s_string in string:
            string = string.replace(first_s_string, second_s_string)
            print(string)
    elif this_command == "Alteration":
        substring = splitted_command[1]
        if substring in string:
            string = string.replace(substring, "")
        print(string)
    else:
        print(f"The spell did not work!")
    command = input()
