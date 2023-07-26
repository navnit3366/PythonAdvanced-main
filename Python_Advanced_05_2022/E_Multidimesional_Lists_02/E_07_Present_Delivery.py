def valid_coordinates(ro, co):
    if 0 <= ro < size and 0 <= co < size:
        return True
    else:
        return False


def move(sa_r, sa_c, comm):
    poss_next_r, poss_next_c = None, None
    if command == "up":
        poss_next_r, poss_next_c = sa_r - 1, sa_c
    elif command == "down":
        poss_next_r, poss_next_c = sa_r + 1, sa_c
    elif command == "left":
        poss_next_r, poss_next_c = sa_r, sa_c - 1
    elif command == "right":
        poss_next_r, poss_next_c = sa_r, sa_c + 1
    if valid_coordinates(poss_next_r, poss_next_c):
        return poss_next_r, poss_next_c
    else:
        return False, False


def gifts_for_all(c_s_row, c_s_col):
    possible_locations = [
        [c_s_row + 1, c_s_col],
        [c_s_row - 1, c_s_col],
        [c_s_row, c_s_col - 1],
        [c_s_row, c_s_col + 1]
    ]
    good_locations = []
    for point_r, point_c in possible_locations:
        if valid_coordinates(point_r, point_c):
            if neighborhood[point_r][point_c] == "V" or neighborhood[point_r][point_c] == "X":
                good_locations.append([point_r, point_c])

    return good_locations


presents = int(input())
no_more_presents = False
size = int(input())
s_r, s_c = None, None
neighborhood = []
nice_kids_count = 0
initial_nice_kids = 0
for row in range(size):
    row_data = input().split()
    for col in range(len(row_data)):
        if row_data[col] == "S":
            s_r, s_c = row, col
        if row_data[col] == "V":
            nice_kids_count += 1
            initial_nice_kids += 1
    neighborhood.append(row_data)

command = input()

while command != "Christmas morning":
    neighborhood[s_r][s_c] = "-"
    pos_r, pos_c = move(s_r, s_c, command)
    s_r, s_c = pos_r, pos_c
    if neighborhood[s_r][s_c] == "V":
        presents -= 1
        nice_kids_count -= 1
        if presents == 0:
            no_more_presents = True
            neighborhood[s_r][s_c] = "S"
            break
    elif neighborhood[s_r][s_c] == "C":
        to_deliver_cookies = gifts_for_all(s_r, s_c)
        for loc_r, loc_c in to_deliver_cookies:
            if neighborhood[loc_r][loc_c] == "X":
                nice_kids_count += 1
            neighborhood[loc_r][loc_c] = "-"
            presents -= 1
            nice_kids_count -= 1
            if presents == 0:
                no_more_presents = True
                break
    neighborhood[s_r][s_c] = "S"
    if no_more_presents:
        break
    command = input()

if presents == 0 and nice_kids_count > 0:
    print(f"Santa ran out of presents!")
for street in neighborhood:
    print(' '.join(street))
if nice_kids_count == 0:
    print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")

