def setup(fld, rovr, sze):
    for r in range(sze):
        data = input().split(" ")
        for c in range(sze):
            if data[c] == "E":
                rovr = [r, c]
        fld.append(data)
    return fld, rovr


def check_position(pos):
    for i in range(len(pos)):
        if pos[i] < 0:
            pos[i] = size-1
        elif pos[i] == size:
            pos[i] = 0
    return pos


def move(fld, rovr,  cmd):
    row = rover[0]
    col = rovr[1]
    if cmd == "up":
        row -= 1
    elif cmd == "down":
        row += 1
    elif cmd == "left":
        col -= 1
    elif cmd == "right":
        col += 1
    row, col = check_position([row, col])
    return row, col


size = 6
field = []
rover = []
field, rover = setup(field, rover, size)
water = []
metal = []
concrete = []
rock = False
commands = input().split(", ")
for command in commands:
    old_r, old_c = rover
    rover = move(field, rover, command)
    new_r, new_c = rover
    if field[new_r][new_c] == "R":
        rock = True
        print(f"Rover got broken at ({new_r}, {new_c})")
        break
    elif field[new_r][new_c] == "W":
        water.append(rover)
        print(f"Water deposit found at ({new_r}, {new_c})")
    elif field[new_r][new_c] == "M":
        metal.append(rover)
        print(f"Metal deposit found at ({new_r}, {new_c})")
    elif field[new_r][new_c] == "C":
        concrete.append(rover)
        print(f"Concrete deposit found at ({new_r}, {new_c})")

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

