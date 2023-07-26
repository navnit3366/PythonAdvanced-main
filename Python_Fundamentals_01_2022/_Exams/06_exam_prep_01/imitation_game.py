message = input()
command = input()
while command != "Decode":
    current_command = command.split("|")
    if current_command[0] == "Move":
        number_of_letters = int(current_command[1])
        letters_to_move_back = message[:number_of_letters]
        letters_to_move_forward = message[number_of_letters:]
        message = letters_to_move_forward + letters_to_move_back
        # print(message)
    elif current_command[0] == "Insert":
        insert_index = int(current_command[1])
        insert_value = current_command[2]
        first_part = message[:insert_index]
        end_part = message[insert_index:]
        message = first_part + insert_value + end_part
        # print(message)
    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        message = message.replace(substring, replacement)
        # print(message)
    command = input()
print(f"The decrypted message is: {message}")
