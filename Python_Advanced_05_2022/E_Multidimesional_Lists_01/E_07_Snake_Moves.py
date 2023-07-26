rows, columns = [int(x) for x in input().split()]
string = input()
counter = 0
matrix = []
for row in range(rows):
    current_row = [None] * columns
    start, end, step = (0, columns, 1) if row % 2 == 0 else (-1, -1 * (columns+1), -1)
    for column in range(start, end, step):
        current_row[column] = (string[counter % len(string)])  # kogato delim procentno poluchavame neobhodimia index !
        counter += 1
    print(''.join(current_row))
