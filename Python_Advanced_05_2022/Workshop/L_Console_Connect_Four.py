def create_start_field(r, c):
    return [[None] * c for x in range(r)]


def print_field(field):
    print(f"i  {'. '.join([str(x+1) for x in range(len(field[0]))])}.")
    for r in range(len(field)):
        print(f"{r+1}. {', '.join([str(0) if not x else str(x) for x in (field[r])])}")


def get_player_move(pl):
    chosen_column = int(input(f"Player {pl}, choose column --> :"))
    return chosen_column - 1


def player_position(field, player, mapper, chosen_column):
    row = mapper[chosen_column]
    mapper[chosen_column] -= 1
    field[row][chosen_column] = player
    return row, chosen_column


def is_win(player, pl_pos, field):
    pl_row = pl_pos[0]
    pl_col = pl_pos[1]

    def normalize_pl_position_by_direction(field, row, column, direction):
        row_dir, col_dir = direction
        row_dir *= -1
        col_dir *= -1
        rows_min_boundary = 0
        cols_min_boundary = 0
        rows_max_boundary = len(field)
        cols_max_boundary = len(field[0])

        # next_row = row
        # next_col = column
        while rows_min_boundary <= row < rows_max_boundary and cols_min_boundary <= column < cols_max_boundary:
            if field[row][column] != player:
                break
            row += row_dir
            column += col_dir

        return row - row_dir, column - col_dir

    def check_win_by_direction(field, init_row, init_column, direction):
        row_dir, col_dir = direction
        row, column = normalize_pl_position_by_direction(field, init_row, init_column, direction)
        row_boundary = min(pl_row + 4 * row_dir, (len(field)))
        col_boundary = min(pl_col + 4 * col_dir, (len(field[0])))

        is_row_included = row_boundary == row
        is_col_included = col_boundary == column

        counter = 0
        while (row != row_boundary or is_row_included) and (column != col_boundary or is_col_included) and player == \
                field[row][column]:
            counter += 1
            row += row_dir
            column += col_dir
        return counter == 4

    h_delta = (0, 1)
    v_delta = (1, 0)
    d_r_delta = (1, 1)
    d_l_delta = (-1, 1)

    return check_win_by_direction(field, pl_row, pl_col, h_delta) \
           or check_win_by_direction(field, pl_row, pl_col, v_delta) \
           or check_win_by_direction(field, pl_row, pl_col, d_r_delta) \
           or check_win_by_direction(field, pl_row, pl_col, d_l_delta)


def play(field):
    current_player = 1
    other_player = 2

    while True:
        player_move = get_player_move(current_player)
        position = player_position(play_field, current_player, row_map, player_move)
        print("-" * 20)
        print_field(play_field)
        if is_win(current_player, position, play_field):
            # print_field(field)
            print()
            print("=="*10)
            print()
            print(f"Player{current_player} win !")
            break
        else:
            current_player, other_player = other_player, current_player


play_field = create_start_field(6, 7)
print_field(play_field)
row_map = [len(play_field) - 1 for x in range(len(play_field[0]))]
play(play_field)
# print_field(play_field)

# print(True,
#       is_win(
#           1,  # player
#           (5, 0),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 0, 0, 0],
#           ]
#       ))
#
# print(True,
#       is_win(
#           1,  # player
#           (2, 0),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#               [1, 0, 1, 0, 0, 0, 0],
#               [1, 1, 0, 0, 0, 0, 0],
#               [1, 0, 1, 1, 0, 0, 0],
#           ]
#       ))
#
# print(True,
#       is_win(
#           1,  # player
#           (1, 0),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#               [0, 1, 0, 0, 0, 0, 0],
#               [0, 0, 1, 0, 0, 0, 0],
#               [0, 0, 0, 1, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#           ]
#       ))
# print(True,
#       is_win(
#           1,  # player
#           (5, 0),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 1, 0, 0, 0],
#               [0, 0, 1, 0, 0, 0, 0],
#               [0, 1, 0, 1, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#           ]
#       ))
#
# print("*" * 50)
#
# print(True,
#       is_win(
#           1,  # player
#           (5, 1),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 0, 0, 0],
#           ]
#       ))
#
# print(True,
#       is_win(
#           1,  # player
#           (3, 0),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#               [1, 0, 1, 0, 0, 0, 0],
#               [1, 1, 0, 0, 0, 0, 0],
#               [1, 0, 1, 1, 0, 0, 0],
#           ]
#       ))
#
# print(True,
#       is_win(
#           1,  # player
#           (3, 2),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#               [0, 1, 0, 0, 0, 0, 0],
#               [0, 0, 1, 0, 0, 0, 0],
#               [0, 0, 0, 1, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#           ]
#       ))
# print(True,
#       is_win(
#           1,  # player
#           (3, 2),  # player_pos
#           [
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 1, 0, 0, 0],
#               [0, 0, 1, 0, 0, 0, 0],
#               [0, 1, 0, 1, 0, 0, 0],
#               [1, 0, 0, 0, 0, 0, 0],
#           ]
#       ))
