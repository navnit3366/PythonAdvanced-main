size = int(input())
field = []
b_r, b_c = None, None
for r in range(size):
    input_row = list(input().split())
    add_row = []
    for i in range(size):
        if input_row[i].isalpha():
            add_row.append(input_row[i])
            if input_row[i] == "B":
                b_r, b_c = r, i
        else:
            add_row.append(int(input_row[i]))
    field.append(add_row)
max_way = None
max_sum = 0
max_points = []

row_left = []
sum_left = 0
for i in range(b_c-1, -1, -1):
    if field[b_r][i] != "X":
        row_left.append([b_r, i])
        sum_left += field[b_r][i]
    else:
        break
max_way = "left"
max_sum = sum_left
max_points = row_left

row_right = []
sum_right = 0
for i in range(b_c+1, size, 1):
    if field[b_r][i] != "X":
        row_right.append([b_r, i])
        sum_right += field[b_r][i]
    else:
        break
if sum_right > max_sum:
    max_way = "right"
    max_sum = sum_right
    max_points = row_right


row_up = []
sum_up = 0
for row in range(b_r-1, -1, -1):
    if field[row][b_c] != "X":
        row_up.append([row, b_c])
        sum_up += field[row][b_c]
    else:
        break
if sum_up > max_sum:
    max_way = "up"
    max_sum = sum_up
    max_points = row_up

row_down = []
sum_down = 0

for row in range(b_r+1, size, 1):
    if field[row][b_c] != "X":
        row_down.append([row, b_c])
        sum_down += field[row][b_c]
    else:
        break
if sum_down > max_sum:
    max_way = "down"
    max_sum = sum_down
    max_points = row_down

print(max_way)
for row in max_points:
    print(row)
print(max_sum)
