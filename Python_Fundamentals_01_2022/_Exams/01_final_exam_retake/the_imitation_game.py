e_message = input()
command = input()

while command != "Decode":
    s_command = command.split("|")
    if s_command[0] == "Move":
        n_letters = int(s_command[1])
        new_first_part = e_message[n_letters:]
        new_second_part = e_message[:n_letters]
        e_message = new_first_part + new_second_part
    elif s_command[0] == "Insert":
        index = int(s_command[1])
        value = s_command[2]
        e_message = e_message[:index] + value + e_message[index:]
    elif s_command[0] == "ChangeAll":
        substring = s_command[1]
        replacement = s_command[2]
        e_message = e_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {e_message}")
