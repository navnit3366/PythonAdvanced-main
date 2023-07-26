def valid_coordinates(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    else:
        return False


size = int(input())
matrix = []
for row in range(size):
    matrix.append([int(x) for x in input().split()])
command = input().split()
while command[0] != "END":
    this_command = command.pop(0)
    ro, co, val = [int(x) for x in command]
    if not valid_coordinates(ro, co, size):
        print(f"Invalid coordinates")
    if valid_coordinates(ro, co, size) and this_command == "Add":
        matrix[ro][co] += val
    elif valid_coordinates(ro, co, size) and this_command == "Subtract":
        matrix[ro][co] -= val
    command = input().split()
for row in matrix:
    print(' '.join([str(x) for x in row]))
