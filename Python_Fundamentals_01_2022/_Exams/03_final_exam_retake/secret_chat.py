message = input()
command = input()
while command != "Reveal":
    split_command = command.split(":|:")
    current_command = split_command[0]
    if current_command == "InsertSpace":
        c_index = int(split_command[1])
        if 0 <= c_index <= len(message):
            message = message[:c_index] + " " + message[c_index:]
            print(message)
    elif current_command == "Reverse":
        c_substring = split_command[1]
        if c_substring in message:
            message = message.replace(c_substring, "", 1)
            message = message + c_substring[::-1]
            print(message)
        else:
            print(f"error")
    elif current_command == "ChangeAll":
        c_substring = split_command[1]
        c_new_substring = split_command[2]
        message = message.replace(c_substring, c_new_substring)
        print(message)
    command = input()
print(f"You have a new text message: {message}")
