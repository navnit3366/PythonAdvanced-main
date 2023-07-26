from mailcap import subst

string = input()

command = input()
while command != "Done":
    s_command = command.split()
    current_comm  = s_command[0]
    if current_comm == "TakeOdd":
        new_str = ""
        for idx in range(len(string)):
            if idx % 2 != 0:
                new_str += string[idx]
        string = new_str
        print(string)
    elif current_comm == "Cut":
        c_index = int(s_command[1])
        c_length = int(s_command[2])
        search_string = string[c_index:(c_index + c_length)]
        string = string.replace(search_string, "", 1)
        print(string)
    elif current_comm == "Substitute":
        substring = s_command[1]
        substitute = s_command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {string}")

