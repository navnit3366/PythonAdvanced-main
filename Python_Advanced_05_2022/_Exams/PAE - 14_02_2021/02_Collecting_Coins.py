import math


def setup(pl_field, field_size, poss):
    for row in range(field_size):
        data = [x for x in input().split()]
        for col in range(field_size):
            if data[col] == "P":
                poss = [row, col]
        pl_field.append(data)
    return poss


def move(f, row, col, comm):
    if comm == "up":
        row -= 1
        if row < 0:
            row = len(f) - 1
    elif comm == "down":
        row += 1
        if row == len(f):
            row = 0
    if comm == "left":
        col -= 1
        if col < 0:
            col = len(f) - 1
    elif comm == "right":
        col += 1
        if col == len(f):
            col = 0
    return row, col


def collect_coins(pl_field, poss, comm, wall_hit, coin):
    row = poss[0]
    col = poss[1]
    row, col = move(pl_field, row, col, comm)
    cell_value = pl_field[row][col]
    if cell_value.isalpha():
        if cell_value == "X":
            wall_hit = "True"
        return 0, [row, col], wall_hit
    else:
        return int(cell_value), [row, col], wall_hit


size = int(input())
field = []
player = [None, None]
player = setup(field, size, player)
# print(field)
# print(size)
# print(player)
coins = 0
command = input()
wall = False
path = [[player[0], player[1]]]
while True:
    field[player[0]][player[1]] = "P"
    new_coins = 0
    new_coins, player, wall = collect_coins(field, player, command, wall, coins)
    path.append(player)

    if wall:
        coins = coins / 2
        break

    coins += new_coins
    if coins >= 100:
        break

    command = input()


if coins >= 100:
    print(f"You won! You've collected {int(math.floor(coins))} coins.")
else:
    print(f"Game over! You've collected {int(math.floor(coins))} coins.")

print("Your path:")

for r in path:
    print(r)