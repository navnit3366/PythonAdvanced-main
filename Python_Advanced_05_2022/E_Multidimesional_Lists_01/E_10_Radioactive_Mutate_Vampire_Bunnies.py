def get_next_position(ro_p, co_p, comm):
    if comm == "U":
        return [ro_p - 1, co_p]
    elif comm == "L":
        return [ro_p, co_p - 1]
    elif comm == "R":
        return [ro_p, co_p + 1]
    elif comm == "D":
        return [ro_p + 1, co_p]


def is_outside(r, c, limit_r, limit_c):
    if 0 <= r < limit_r and 0 <= c < limit_c:
        return False
    else:
        return True


def get_childs(ro_b, co_b, limit_ro, limit_co):
    coordinates = [
        [ro_b - 1, co_b],
        [ro_b, co_b - 1],
        [ro_b, co_b + 1],
        [ro_b + 1, co_b]
    ]

    result = []

    for point_r, point_c in coordinates:
        if not is_outside(point_r, point_c, limit_ro, limit_co):
            result.append([point_r, point_c])

    return result

ro, co = [int(x) for x in input().split()]
matrix = []
won_flag = False
dead_flag = False
pl_ro = None
pl_co = None
bunnies = set()
for row in range(ro):
    this_row = list(input())
    for co_ in range(len(this_row)):
        if this_row[co_] == "P":
            pl_ro = row
            pl_co = co_
        elif this_row[co_] == "B":
            bunnies.add(f"{row} {co_}")
    matrix.append(this_row)

commands = input()
for command in commands:
    next_pl_ro, next_pl_co = get_next_position(pl_ro, pl_co, command)
    matrix[pl_ro][pl_co] = "."

    if is_outside(next_pl_ro, next_pl_co, ro, co):
        won_flag = True
    elif matrix[next_pl_ro][next_pl_co] == "B":
        dead_flag = True
        pl_ro, pl_co = next_pl_ro, next_pl_co
    else:
        matrix[next_pl_ro][next_pl_co] = "P"
        pl_ro, pl_co = next_pl_ro, next_pl_co

    new_bunnies = set()

    for bun in bunnies:
        b_r, b_c = [int(x) for x in bun.split()]
        b_childs = get_childs(b_r, b_c, ro, co)
        for child_r, child_c in b_childs:
            new_bunnies.add(f"{child_r} {child_c}")
            matrix[child_r][child_c] = "B"
            if child_r == pl_ro and child_c == pl_co:
                dead_flag = True
    bunnies = bunnies.union(new_bunnies)

    if won_flag or dead_flag:
        break

for row in matrix:
    print(''.join(row))

if won_flag:
    print(f"won: {pl_ro} {pl_co}")
if dead_flag:
    print(f"dead: {pl_ro} {pl_co}")
