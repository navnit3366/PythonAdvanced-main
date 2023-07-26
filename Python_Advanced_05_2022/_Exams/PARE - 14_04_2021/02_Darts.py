from collections import deque


def field_setup(f_as_matrix):
    for r in range(7):
        row_data = [x for x in input().split()]
        f_as_matrix.append(row_data)
    return f_as_matrix


def get_throw():
    throw_list = []
    string = input()
    while string:
        string = string[1:-1].split(", ")
        throw_list.append([int(x) for x in string])
        string = input()
    return deque(throw_list)


# print(get_throw())


def sum_of_border_values(g_field, row, col):
    left_value = int(g_field[row][0])
    right_value = int(g_field[row][6])
    up_value = int(g_field[0][col])
    down_value = int(g_field[6][col])
    border_sum = left_value + right_value + up_value + down_value
    return border_sum


def check_points(g_field, row, col):
    if 0 <= row <= 6 and 0 <= col <= 6:
        field_value = g_field[row][col]
        if field_value.isdigit():
            return int(field_value)
        elif field_value == "D":
            special_point = sum_of_border_values(g_field, row, col)
            return 2 * special_point
        elif field_value == "T":
            special_point = sum_of_border_values(g_field, row, col)
            return 3 * special_point
        elif field_value == "B":
            return 100000
    else:
        return 0


current_player, other_player = input().split(", ")

current_player_points = 501
other_player_points = 501
current_player_counter = 0
other_player_counter = 0

field = []
field_setup(field)

# throw = get_throw()

while True:
    # current_r, current_col = throw.popleft()
    current_r, current_col = [int(x) for x in input()[1:-1].split(", ")]
    current_player_counter += 1
    current_points = check_points(field, current_r, current_col)
    current_player_points -= current_points
    if current_player_points <= 0:
        break
    # if not throw:
    #     break
    current_player, other_player = other_player, current_player
    current_player_points, other_player_points = other_player_points, current_player_points
    current_player_counter, other_player_counter = other_player_counter, current_player_counter

print(f"{current_player} won the game with {current_player_counter} throws!")

