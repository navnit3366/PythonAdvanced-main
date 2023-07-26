def setup(siz):
    fld = []
    pos = []
    for r in range(siz):
        data = input().split(" ")
        for c, value in enumerate(data):
            if value == "A":
                pos = [r, c]
        fld.append(data)
    return fld, pos


def print_field(fld):
    for r in fld:
        print(" ".join(r))


def out_of_range(pos):
    row, col = pos[0], pos[1]
    if 0 <= row < size and 0 <= col < size:
        return False
    return True


def move(cmd, pos):
    delta = []
    if cmd == "up":
        delta = [-1, 0]
    elif cmd == "down":
        delta = [1, 0]
    elif cmd == "left":
        delta = [0, -1]
    elif cmd == "right":
        delta = [0, 1]
    pos_r = pos[0] + delta[0]
    pos_c = pos[1] + delta[1]
    return [pos_r, pos_c]


size = int(input())
field, position = setup(size)
loose = False
teabags = 0
command = input()
field[position[0]][position[1]] = "*"
while command:
    old_r, old_c = position
    position = move(command, position)
    if out_of_range(position):
        loose = True
        break
    new_r, new_c = position
    if field[new_r][new_c] == "R":
        loose = True
        field[new_r][new_c] = "*"
        break
    elif field[new_r][new_c].isdigit():
        teabags += int(field[new_r][new_c])
    field[new_r][new_c] = "*"
    if teabags >= 10:
        break
    command = input()

if loose:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print_field(field)
