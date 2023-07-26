def boundary_check(index):
    if index > len(field)-1:
        return 0
    elif index < 0:
        return len(field)-1
    return index


def move(position, direction):
    delta_up = (-1, 0)
    delta_down = (1, 0)
    delta_left = (0, -1)
    delta_right = (0, 1)

    if direction == "up":
        rover_r = boundary_check(position[0] + delta_up[0])
        rover_c = boundary_check(position[1] + delta_up[1])
    elif direction == "down":
        rover_r = boundary_check(position[0] + delta_down[0])
        rover_c = boundary_check(position[1] + delta_down[1])
    elif direction == "left":
        rover_r = boundary_check(position[0] + delta_left[0])
        rover_c = boundary_check(position[1] + delta_left[1])
    else:
        rover_r = boundary_check(position[0] + delta_right[0])
        rover_c = boundary_check(position[1] + delta_right[1])
    return [rover_r, rover_c]


def area_quality_check(wat, met, conc):
    if all([wat, met, conc]):
        print("Area suitable to start the colony.")
    else:
        print("Area not suitable to start the colony.")


field = []
water = None
concrete = None
metal = None
rover_position = [0, 0]

for r in range(6):
    row_data = [x for x in input().split(" ")]
    for c in range(6):
        if row_data[c] == "E":
            rover_position = [r, c]
    field.append(row_data)

commands = input().split(", ")

# for r in range(6):
#     print(" ".join([x for x in field[r]]))

for command in commands:
    rover_position = move(rover_position, command)
    ro_r, ro_c = rover_position

    if field[ro_r][ro_c] == "R":
        print(f"Rover got broken at ({ro_r}, {ro_c})")
        break
    elif field[ro_r][ro_c] == "W":
        water = True
        print(f"Water deposit found at ({ro_r}, {ro_c})")
    elif field[ro_r][ro_c] == "M":
        metal = True
        print(f"Metal deposit found at ({ro_r}, {ro_c})")
    elif field[ro_r][ro_c] == "C":
        concrete = True
        print(f"Concrete deposit found at ({ro_r}, {ro_c})")

area_quality_check(water, metal, concrete)
