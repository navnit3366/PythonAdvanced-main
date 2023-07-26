def setup_field(siz):
    fld = []
    snk = []
    burrow = []
    for r in range(siz):
        data = list(input())
        for c in range(siz):
            if data[c] == "S":
                snk = [r, c]
            elif data[c] == "B":
                burrow.append([r, c])
        fld.append(data)
    return fld, snk, burrow


def move(fild, r, c, comm, out_of_fld):
    if comm == "up":
        r -= 1
    elif comm == "down":
        r += 1
    elif comm == "left":
        c -= 1
    elif comm == "right":
        c += 1
    if 0 <= r < len(fild) and 0 <= c < len(fild):
        out_of_fld = False
    else:
        out_of_fld = True
    return [r, c], out_of_fld


def find_which_burrow(snk, brrw):
    if snk == brrw[0]:
        s_in = brrw[0]
        s_out = brrw[1]
    else:
        s_in = brrw[1]
        s_out = brrw[0]
    return s_in, s_out


size = int(input())
field = []
snake = []
burrow = []
field, snake, burrow = setup_field(size)
out = False
food = 0
win = False
command = input()
while True:
    old_r = snake[0]
    old_c = snake[1]
    snake, out = move(field, old_r, old_c, command, out)
    field[old_r][old_c] = "."

    if out:
        break

    if snake in burrow:
        burrow_in, burrow_out = find_which_burrow(snake, burrow)
        field[burrow_in[0]][burrow_in[1]] = "."
        snake = burrow_out
        burrow = []

    row, col = snake

    if field[row][col] == "*":
        food += 1

    field[snake[0]][snake[1]] = "S"

    if food == 10:
        win = True
        break

    command = input()

if out:
    print("Game over!")
if win:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")

for r in field:
    print(f"{''.join(r)}")
