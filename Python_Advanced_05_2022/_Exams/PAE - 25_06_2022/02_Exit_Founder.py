def setup(sze):
    fld = []
    for r in range(sze):
        fld.append(input().split(" "))
    return fld


size = 6
current, other = input().split(", ")
field = setup(size)

command = [int(x) for x in input()[1:-1].split(", ")]
skip = []

while True:
    row = command[0]
    col = command[1]
    if current in skip:
        skip.remove(current)
        current, other = other, current
        command = [int(x) for x in input()[1:-1].split(", ")]
        continue
    if field[row][col] == "W":
        skip.append(current)
        print(f"{current} hits a wall and needs to rest.")
    elif field[row][col] == "E":
        print(f"{current} found the Exit and wins the game!")
        break
    elif field[row][col] == "T":
        print(f"{current} is out of the game! The winner is {other}.")
        break

    current, other = other, current
    command = [int(x) for x in input()[1:-1].split(", ")]
