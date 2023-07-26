def identical_values_square(n, m):
    value1 = matrx[n][m]
    value2 = matrx[n][m+1]
    value3 = matrx[n+1][m]
    value4 = matrx[n+1][m+1]
    if value1 == value2 and value1 == value3 and value3 == value4:
        return True
    else:
        return False


rows, columns = [int(x) for x in input().split()]
matrx = []
for row in range(rows):
    matrx.append(input().split())

counter = 0

for i in range(len(matrx) - 1):
    for j in range(len(matrx[i]) - 1):
        if identical_values_square(i, j):
            counter += 1

print(counter)
