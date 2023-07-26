def setup(size):
    fld = []
    pos = []
    targets = 0
    for r in range(size):
        data = input().split()
        for c, val in enumerate(data):
            if val == "A":
                pos = [r, c]
            if val == "x":
                targets += 1
        fld.append(data)
    return fld, pos, targets


def move(fld, pos, cmd):
    delta = []
    row = pos[0]
    col = pos[1]
    direction = cmd[1]
    steps = int(cmd[2])
    if direction == "right":
        delta = [0, 1]
    elif direction == "left":
        delta = [0, -1]
    elif direction == "up":
        delta = [-1, 0]
    elif direction == "down":
        delta = [1, 0]
    for i in range(steps):
        if row+delta[0] == sze:
            break
        elif col+delta[1] == sze:
            break
        elif row+delta[0] < 0:
            break
        elif col+delta[1] < 0:
            break
        elif fld[row+delta[0]][col+delta[1]] == "x":
            break
        row += delta[0]
        col += delta[1]

    pos = [row, col]
    return fld, pos


def shoot(fld, pos, cmd):
    delta = []
    trgt = []
    row = pos[0]
    col = pos[1]
    direction = cmd[1]

    if direction == "right":
        delta = [0, 1]
    elif direction == "left":
        delta = [0, -1]
    elif direction == "up":
        delta = [-1, 0]
    elif direction == "down":
        delta = [1, 0]
    for i in range(sze):
        row += delta[0]
        col += delta[1]
        if 0 <= row < sze and 0 <= col < sze:
            if fld[row][col] == "x":
                trgt = [row, col]
                break
    return fld, trgt

all_targets = 0
field = []
position = []
sze = 5
field, position, all_targets = setup(sze)
hit = []
target = []


number_of_commands = int(input())
for _ in range(number_of_commands):
    target = []
    old_r, old_c = position
    command = input().split()

    if command[0] == "move":
        field, position = move(field, position, command)

    elif command[0] == "shoot":
        field, target = shoot(field, position, command)

    new_r, new_c = position
    field[old_r][old_c] = "."
    if target:
        target_r, target_c = target
        hit.append(target)
        field[target_r][target_c] = "."
    field[new_r][new_c] = "A"

if len(hit) == all_targets:
    print(f"Training completed! All {all_targets} targets hit.")
else:
    print(f"Training not completed! {all_targets - len(hit)} targets left.")
for row in hit:
    print(row)
for row in field:
    print(row)