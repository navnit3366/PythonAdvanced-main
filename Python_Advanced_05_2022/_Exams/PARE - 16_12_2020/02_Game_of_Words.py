def setup(siz, plr):
    fld = []
    for row in range(siz):
        data = list(input())
        for i in range(siz):
            if data[i] == "P":
                plr = [row, i]
                break
        fld.append(data)
    return fld, plr


def check_out_of_field(r, c):
    if -1 < r < size and -1 < c < size:
        return False
    return True


def move(plr, ou, comm):
    r = plr[0]
    c = plr[1]
    if comm == "up":
        r -= 1
    elif comm == "down":
        r += 1
    elif comm == "left":
        c -= 1
    elif comm == "right":
        c += 1
    ou = check_out_of_field(r, c)
    if ou:
        return plr, ou
    plr = [r, c]
    return plr, ou


string = input()
size = int(input())
player = []
out = False

field, player = setup(size, player)
commands_number = int(input())

for comm in range(commands_number):
    command = input()
    old_r, old_c = player
    player, out = move(player, out, command)
    row, col = player
    if out:
        string = string[:-1]
    else:
        if field[row][col] != "-":
            string += field[row][col]
        field[old_r][old_c] = "-"
        field[row][col] = "P"

print(string)
for r in range(size):
    print(''.join(field[r]))


