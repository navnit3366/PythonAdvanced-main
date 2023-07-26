import os


def create_empty_file(filename):
    file = open(filename, "w")
    file.close()


def add_file_content(filename, content):
    with open(filename, "a") as file:
        file = open(filename, "a")
        file.writelines(content)
        file.writelines("\n")


def replace_string_in_file(filename, old_string, new_string):
    try:
        with open(filename, "r") as file:
            string = file.read()
            string_to_write = string.replace(old_string, new_string)
        with open(filename, "w") as file:
            file.write(string_to_write)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("An error occurred")


command = input()
while command != "End":
    split_command = command.split("-")
    this_command = split_command[0]
    f_name = split_command[1]
    if this_command == "Create":
        create_empty_file(f_name)
    elif this_command == "Add":
        f_content = split_command[2]
        add_file_content(f_name, f_content)
    elif this_command == "Replace":
        f_old_String = split_command[2]
        f_new_String = split_command[3]
        replace_string_in_file(f_name, f_old_String, f_new_String)
    elif this_command == "Delete":
        delete_file(f_name)
    command = input()
