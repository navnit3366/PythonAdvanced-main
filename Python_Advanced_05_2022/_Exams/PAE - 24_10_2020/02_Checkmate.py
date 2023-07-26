def setup(fld, siz, k):
    for row in range(siz):
        data = input().split()
        fld.append(data)
        for col in range(len(data)):
            if data[col] == "K":
                k = [row, col]
    return fld, k


def check_for_capture(kng, fld, siz):
    killer_queens = []
    k_row = kng[0]
    k_col = kng[1]
    deltas = [[-1, -1], [-1, 1], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [1, 0] ]

    for delta in deltas:
        d_r = delta[0]
        d_c = delta[1]
        this_r = k_row
        this_c = k_col
        for r in range(siz):
            this_r += d_r
            this_c += d_c
            if 0 <= this_r < size and 0 <= this_c < size:
                if fld[this_r][this_c] == "Q":
                    killer_queens.append([this_r, this_c])
                    break

    return killer_queens


size = 8
field = []
king = []
field, king = setup(field, size, king)
queens = check_for_capture(king, field, size)
if queens:
    for q in queens:
        print(q)
else:
    print("The king is safe!")
