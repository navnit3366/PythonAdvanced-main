def get_children(mat, row, col):
    coordinates = [
        [row-1, col-1],
        [row-1, col],
        [row-1, col+1],
        [row, col-1],
        [row, col+1],
        [row+1, col-1],
        [row+1, col],
        [row+1, col+1],
    ]
    child_cels = []
    for row, col in coordinates:
        if 0 <= row < len(matrix) and 0 <= col < len(matrix) and mat[row][col] > 0:
            child_cels.append([row, col])
    return child_cels
'''
Extremley good way to find cell childrens with this matrx :)
'''

size = int(input())
matrix = []
for ro in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()
for bomb in bombs:
    r, c = [int(x) for x in bomb.split(",")]
    bomb_value = matrix[r][c]
    matrix[r][c] = 0
    children_s_matrx = get_children(matrix, r, c)
    for ro, co in children_s_matrx:
        matrix[ro][co] -= bomb_value

alive = 0
alive_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 0:
            alive += 1
            alive_sum += matrix[i][j]
print(f"Alive cells: {alive}")
print(f"Sum: {alive_sum}")
for row in range(len(matrix)):
    print(' '.join([str(x) for x in matrix[row]]))
