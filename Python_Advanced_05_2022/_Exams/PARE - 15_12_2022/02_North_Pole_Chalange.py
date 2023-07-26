def setup(matrx, rows, decor, gift, cookie, poss):
    for row in range(rows):
        row_data = input().split()
        for col in range(len(row_data)):
            if row_data[col] == "Y":
                poss = [row, col]
            elif row_data[col] == "D":
                decor.append([row, col])
            elif row_data[col] == "G":
                gift.append([row, col])
            elif row_data[col] == "C":
                cookie.append([row, col])
        matrx.append(row_data)
    return matrx, decor, gift, cookie, poss


def delta(dir_):
    size = int(dir_[1])
    res = []
    if dir_[0] == "right":
        res = [0, 1 * size]
    elif dir_[0] == "left":
        res = [0, -1 * size]
    elif dir_[0] == "up":
        res = [-1 * size, 0]
    elif dir_[0] == "down":
        res = [1 * size, 0]
    return res


def out_of_border_check(poss, matr):
    ro, co = poss
    ro = ro % len(matr)
    co = co % len(matr[0])
    return ro, co


def move(matrx, direction, poss):
    old_pos = poss.copy()
    delta_row, delta_col = delta(direction)
    way_size = sum([delta_row, delta_col])
    step = abs(way_size) // way_size
    poss[0] += delta_row
    poss[1] += delta_col

    if delta_row != 0:
        for row in range(old_pos[0], poss[0], step):
            row = row % len(matrx)
            col = poss[1]
            temp_position = [row, col]
            items_collector(decorations, gifts, cookies, temp_position, matrx)
            matrx[row][col] = "x"
            if len(decorations) == 0 and len(cookies) == 0 and len(gifts) == 0:
                return matrx, [row, col]

    if delta_col != 0:
        row = poss[0]
        for col in range(old_pos[1], poss[1], step):
            col = col % len(matrx[0])
            temp_position = [row, col]
            items_collector(decorations, gifts, cookies, temp_position, matrx)
            matrx[row][col] = "x"
            if len(decorations) == 0 and len(cookies) == 0 and len(gifts) == 0:
                return matrx, [row, col]

    poss[0], poss[1] = out_of_border_check(poss, matrx)

    return matrx, poss


def items_collector(deco, gift, cookie, poss, matrx):
    if matrx[poss[0]][poss[1]] == "D":
        deco.pop()
    elif matrx[poss[0]][poss[1]] == "G":
        gift.pop()
    elif matrx[poss[0]][poss[1]] == "C":
        cookie.pop()


decorations = []
gifts = []
cookies = []
matrix = []
position = []
m_rows, m_cols = [int(x) for x in input().split(", ")]
matrix, decorations, gifts, cookies, position = setup(matrix, m_rows, decorations, gifts, cookies, position)

all_decorations = len(decorations)
all_gifts = len(gifts)
all_cookies = len(cookies)

command = input().split("-")
while command[0] != "End":
    matrix, position = move(matrix, command, position)
    items_collector(decorations, gifts, cookies, position, matrix)
    matrix[position[0]][position[1]] = "Y"
    if len(decorations) == 0 and len(cookies) == 0 and len(gifts) == 0:
        break
    command = input().split("-")

if len(decorations) == 0 and len(cookies) == 0 and len(gifts) == 0:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {all_decorations - len(decorations)} Christmas decorations")
print(f"- {all_gifts - len(gifts)} Gifts")
print(f"- {all_cookies - len(cookies)} Cookies")

for r in matrix:
    print(' '.join([x for x in r]))
