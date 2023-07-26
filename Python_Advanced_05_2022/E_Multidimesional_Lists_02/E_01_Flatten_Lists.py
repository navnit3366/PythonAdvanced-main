rows_string = input().split("|")
matrix = []
result_matrix = []
for row in rows_string:
    matrix.append(row.split())

for row in range(len(matrix)-1, -1, -1):
    for column in range(len(matrix[row])):
        result_matrix.append(matrix[row][column])
print(' '.join(result_matrix))
