number_of_pieces = int(input())
pieces = {}
for piece in range(number_of_pieces):
    current_input = input().split("|")
    c_piece = current_input[0]
    c_composer = current_input[1]
    c_key = current_input[2]
    pieces[c_piece] = [c_composer, c_key]

command = input()
while command != "Stop":
    s_comm = command.split("|")
    c_command = s_comm[0]
    if c_command == "Add":
        c_piece = s_comm[1]
        c_composer = s_comm[2]
        c_key = s_comm[3]
        if c_piece not in pieces:
            pieces[c_piece] = [c_composer, c_key]
            print(f"{c_piece} by {c_composer} in {c_key} added to the collection!")
        else:
            print(f"{c_piece} is already in the collection!")
    elif c_command == "Remove":
        c_piece = s_comm[1]
        if c_piece not in pieces:
            print(f"Invalid operation! {c_piece} does not exist in the collection.")
        else:
            del pieces[c_piece]
            print(f"Successfully removed {c_piece}!")
    elif c_command == "ChangeKey":
        c_piece = s_comm[1]
        c_new_key = s_comm[2]
        if c_piece not in pieces:
            print(f"Invalid operation! {c_piece} does not exist in the collection.")
        else:
            old_comp_and_key = pieces[c_piece]
            new_comp_and_key = [old_comp_and_key[0], c_new_key]
            pieces[c_piece] = new_comp_and_key
            print(f"Changed the key of {c_piece} to {c_new_key}!")
    command = input()
for piece, composer_key in pieces.items():
    print(f"{piece} -> Composer: {composer_key[0]}, Key: {composer_key[1]}")