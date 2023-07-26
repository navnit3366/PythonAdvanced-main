def setup(matr, shots):
    matr = []
    shots = []
    for row in range(6):
        r = [int(x) if x.isnumeric() else x for x in input().split()]
        matr.append(r)
    for i in range(3):
        string = input()
        string = string[1:-1]
        ro, co = string.split(", ")
        shots.append([int(ro), int(co)])
    return [matr, shots]


def collector(point):
    item = ""
    if 100 <= point <= 199:
        item = "Football"
    elif 200 <= point <= 299:
        item = "Teddy Bear"
    if 300 <= point:
        item = "Lego Construction Set"
    return item


hit = []
field = []
shoots = []
field, shoots = setup(field, shoots)
mid_sum = 0

for shot in shoots:
    shot_row, shot_col = [shot[0], shot[1]]
    if not (-1 < shot_row < 6) or not (-1 < shot_col < 6):
        continue
    if not isinstance(field[shot_row][shot_col], int):
        if [shot_row, shot_col] not in hit:
            hit.append([shot_row, shot_col])
            for row in range(6):
                if isinstance(field[row][shot_col], int):
                    mid_sum += field[row][shot_col]

items = collector(mid_sum)
if items:
    print(f"Good job! You scored {mid_sum} points, and you've won {items}.")
else:
    print(f"Sorry! You need {100 - mid_sum} points more to win a prize.")

