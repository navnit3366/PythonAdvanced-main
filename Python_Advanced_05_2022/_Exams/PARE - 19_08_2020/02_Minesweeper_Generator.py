def setup(size):
    fld = []
    for r in range(size):
        fld.append([])
        for c in range(size):
            fld[r].append(0)
    return fld


def bombs_setup(fld, b_num):
    bombs = []
    for i in range(b_num):
        row, col = [int(x) for x in input()[1:-1].split(", ")]
        fld[row][col] = "*"
        bombs.append([row, col])
    return fld, bombs


def is_in_the_field(fld, row, col):
    if 0 <= row < len(fld) and 0 <= col < len(fld):
        return True
    return False


def add_numbers(fld, bombs):
    waning_fields = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]]
    for bomb in bombs:
        b_r, b_c = bomb[0], bomb[1]
        for warning_field in waning_fields:
            warn_r, warn_col = b_r + warning_field[0], b_c + warning_field[1]
            if is_in_the_field(fld, warn_r, warn_col):
                if fld[warn_r][warn_col] != "*":
                    fld[warn_r][warn_col] += 1
    return fld


def print_fld(fld):
    for r in range(len(fld)):
        print(f"{' '.join([str(x) for x in fld[r]])}")


f_size = int(input())
bombs_count = int(input())
field = setup(f_size)
field, bombs_list = bombs_setup(field, bombs_count)

field = add_numbers(field, bombs_list)
print_fld(field)
