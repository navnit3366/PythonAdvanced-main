rows = int(input())
matrix = []
for r in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

primary_diag = []
second_diag = []

for row in range(rows):
    col_index = rows - row - 1
    primary_diag.append(matrix[row][row])
    second_diag.append(matrix[row][col_index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diag])}. Sum: {sum(primary_diag)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second_diag])}. Sum: {sum(second_diag)}")
