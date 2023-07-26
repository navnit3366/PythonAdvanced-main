def get_magic_triangle(a):
    matr = []
    for row in range(a):
        matr.append([])
        for col in range(0, row+1):
            matr[row].append(1)

    for row in range(2, a):
        for col in range(1, row):
            left = matr[row-1][col-1]
            right = matr[row-1][col]
            matr[row][col] = left + right
    return matr


print(get_magic_triangle(100))
