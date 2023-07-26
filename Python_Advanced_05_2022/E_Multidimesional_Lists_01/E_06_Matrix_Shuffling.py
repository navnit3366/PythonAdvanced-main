rows, columns = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    matrix.append(input().split())

command = input().split()
while command[0] != "END":
    flag = True
    if len(command) == 5:
        txt_command = command.pop(0)
        if txt_command == "swap":
            r1, c1, r2, c2 = [int(x) for x in command]
            if 0 <= r1 < rows or 0 <= r2 < rows:
                if 0 <= c1 < rows or 0 <= c2 < columns:
                    t1 = matrix[r2][c2]
                    t2 = matrix[r1][c1]
                    matrix[r1][c1] = t1
                    matrix[r2][c2] = t2
            else:
                print(f"Invalid input!")
                flag = False
        else:
            print(f"Invalid input!")
            flag = False
    else:
        print(f"Invalid input!")
        flag = False
    if flag:
        for r in range(len(matrix)):
            print(' '.join([str(x) for x in matrix[r]]))
    command = input().split()
