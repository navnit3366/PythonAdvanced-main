def initialize_field(game_field, white_pos, black_pos):
    for r in range(8):
        row_data = input().split(" ")
        game_field.append(row_data)
        for c in range(8):
            if row_data[c] == "b":
                black_pos[0], black_pos[1] = [r, c]
            elif row_data[c] == "w":
                white_pos[0], white_pos[1] = [r, c]
    return game_field, white_pos, black_pos,


def field_with_coordinates():
    coordinated_field = []
    row = 9
    for r in range(8):
        row -= 1
        coordinated_field.append([])
        for c in range(8):
            col = chr(97 + c)
            coordinated_field[r].append(f"{col}{row}")
    return coordinated_field


def new_queen(player_pos):
    player_color = player_pos[2]
    if player_color == "w" and player_pos[0] == 0:
        return True
    if player_color == "b" and player_pos[0] == 7:
        return True


def print_field(fld):
    print("==" * 20)
    [print(' '.join(fld[r])) for r in range(len(fld))]


def player_move(player_position, other_player_pos):
    player_r = player_position[0]
    player_c = player_position[1]
    player_color = player_position[2]
    if player_color == "w":
        move_dir = -1
    else:
        move_dir = 1

    if player_position[2] == "w":
        attack_move = [
            [player_r - 1, player_c - 1],
            [player_r - 1, player_c + 1],
        ]
    else:
        attack_move = [
            [player_r + 1, player_c - 1],
            [player_r + 1, player_c + 1],
        ]
    for move in attack_move:
        if move[1] == -1:
            continue
        elif move[1] == 8:
            continue
        if move[0] == other_player_pos[0] and move[1] == other_player_pos[1]:
            player_position[0] = move[0]
            player_position[1] = move[1]
            return player_position, True

    player_position[0] = player_r + move_dir
    return player_position, False


field = []
coordinates_field = field_with_coordinates()
current_player_pos = [0, 0, "w"]
other_player_pos = [0, 0, "b"]

field, current_player_pos, other_player_pos, = initialize_field(field, current_player_pos, other_player_pos)

win = False
queen = False

while True:
    current_player_pos, win = player_move(current_player_pos, other_player_pos)
    current_row = current_player_pos[0]
    current_col = current_player_pos[1]
    current_color = current_player_pos[2]
    if win:
        field[current_row][current_col] = current_color
        # print_field(field)
        break

    queen = new_queen(current_player_pos)

    if queen:
        field[current_row][current_col] = current_color
        # print_field(field)
        break
    field[current_row][current_col] = current_color
    # print_field(field)
    current_player_pos, other_player_pos = other_player_pos, current_player_pos

color = "White" if current_player_pos[2] == "w" else "Black"
coordinates = coordinates_field[current_player_pos[0]][current_player_pos[1]]

if win:
    print(f"Game over! {color} win, capture on {coordinates}.")
else:
    print(f"Game over! {color} pawn is promoted to a queen at {coordinates}.")
# print(current_player_pos)
