rows = int(input())
matrix = []
for r in range(rows):
    matrix.append([int(x) for x in input().split()])
primary_diag = []
second_diag = []
for row in range(rows):
    primary_diag.append(matrix[row][row])

for ro in range(rows):
    col_index = rows - ro - 1
    second_diag.append(matrix[ro][col_index])

print(abs(sum(primary_diag) - sum(second_diag)))
