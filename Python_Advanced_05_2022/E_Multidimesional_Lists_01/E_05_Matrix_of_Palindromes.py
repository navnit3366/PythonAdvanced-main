rows, columns = [int(x) for x in input().split()]
counter_row = 96
matrix = []
for row in range(rows):
    counter_row += 1
    row_symbol = chr(counter_row)
    current_row = []
    for column in range(columns):
        counter_column = counter_row + column
        column_symbol = chr(counter_column)
        this_string = row_symbol + column_symbol + row_symbol
        current_row.append(this_string)
    matrix.append(current_row)

for r in range(len(matrix)):
    print(' '.join(matrix[r]))