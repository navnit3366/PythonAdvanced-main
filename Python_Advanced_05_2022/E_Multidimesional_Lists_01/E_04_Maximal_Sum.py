def square_sum(m, n, size_):
    sq_sum = 0
    sq_matrix = []
    for r in range(size_):
        row_index = m + r
        r_sub_matrx = []
        for col in range(size_):
            col_index = n + col
            r_sub_matrx.append(matrix[row_index][col_index])
        sq_matrix.append(r_sub_matrx)
        sq_sum += sum(r_sub_matrx)
    return sq_matrix, sq_sum


rows, columns = [int(x) for x in input().split()]
size = 3
matrix = []
max_size_matrix = []
max_sum = -1000000000

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for i in range(rows - (size - 1)):
    for j in range(columns - (size - 1)):
        current_sub_matrix, current_max_sum = square_sum(i, j, size)
        if current_max_sum > max_sum:
            max_size_matrix = current_sub_matrix
            max_sum = current_max_sum
print(f"Sum = {max_sum}")
for r in range(len(max_size_matrix)):
    print(' '.join([str(x) for x in max_size_matrix[r]]))
