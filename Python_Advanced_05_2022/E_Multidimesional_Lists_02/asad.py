field = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
b_r = 1
b_c = 2
row_left = field[b_r][:b_c]
row_right = field[b_r][b_c+1:]
column_all = []
for row in range(len(field)):
    column_all.append(field[row][b_c])
col_up = column_all[:b_r]
col_down = column_all[b_r+1:]
a = 5
