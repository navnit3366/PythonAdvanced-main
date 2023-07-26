def knight_moves(k_row, k_col, matrix_size):
    coordinates = [
        [k_row-2, k_col-1],
        [k_row-2, k_col+1],
        [k_row-1, k_col-2],
        [k_row-1, k_col+2],
        [k_row+1, k_col-2],
        [k_row+1, k_col+2],
        [k_row+2, k_col-1],
        [k_row+2, k_col+1],
    ]
    result = 0
    for point_r, point_c in coordinates:
        if 0 <= point_r < matrix_size and 0 <= point_c < matrix_size:
            if matrix[point_r][point_c] == "K":
                result += 1
    return result


size = int(input())
matrix = []
knights_coordinates = []
removed_knights = 0

for row in range(size):
    row_list = list(input())
    matrix.append(row_list)
    for col in range(len(row_list)):
        if row_list[col] == "K":
            knights_coordinates.append([row, col])

while True:
    max_count = 0
    k_r, k_c = None, None
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "0":
                continue
            count = knight_moves(r, c, size)
            if count > max_count:
                max_count = count
                k_r, k_c = r, c
    if max_count == 0:
        break
    matrix[k_r][k_c] = "0"
    removed_knights += 1

print(removed_knights)
