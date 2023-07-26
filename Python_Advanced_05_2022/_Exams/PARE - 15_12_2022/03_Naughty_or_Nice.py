from collections import deque


def naughty_or_nice_list(santa_list, *commands, **kwargs):
    string = ""
    santa_new_list = deque(santa_list.copy())
    nice = []
    naughty = []
    if commands:
        for command in commands:
            command = command.split("-")
            number = int(command[0])
            k_type = command[1]
            if k_type == "Naughty":
                found_index = None
                naughty_counter = 0
                for index in range(len(santa_new_list)):
                    santa_number = santa_new_list[index][0]
                    if santa_new_list[index][0] == number:
                        naughty_counter += 1
                        found_index = index
                if naughty_counter == 1:
                    naughty.append(santa_new_list[found_index][1])
                    del santa_new_list[found_index]

            elif k_type == "Nice":
                found_index = None
                nice_counter = 0
                for index in range(len(santa_new_list)):
                    santa_number = santa_new_list[index][0]
                    if santa_new_list[index][0] == number:
                        nice_counter += 1
                        found_index = index
                if nice_counter == 1:
                    nice.append(santa_new_list[found_index][1])
                    del santa_new_list[found_index]

    if kwargs:
        for name, kid_type in kwargs.items():
            if kid_type == "Naughty":
                found_index = None
                naughty_counter = 0
                for index in range(len(santa_new_list)):
                    if santa_new_list[index][1] == name:
                        naughty_counter += 1
                        found_index = index
                if naughty_counter == 1:
                    naughty.append(santa_new_list[found_index][1])
                    del santa_new_list[found_index]

            elif kid_type == "Nice":
                found_index = None
                nice_counter = 0
                for index in range(len(santa_new_list)):
                    if santa_new_list[index][1] == name:
                        nice_counter += 1
                        found_index = index
                if nice_counter == 1:
                    nice.append(santa_new_list[found_index][1])
                    del santa_new_list[found_index]

    if nice:
        string += f"Nice: {', '.join(nice)}\n"
    if naughty:
        string += f"Naughty: {', '.join(naughty)}\n"
    if santa_new_list:
        names = []
        for _ in santa_new_list:
            names.append(_[1])
        string += f"Not found: {', '.join(names)}\n"
    # print(nice)
    # print(naughty)
    # print(santa_new_list)
    return string


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print()

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
