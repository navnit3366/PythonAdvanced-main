# a = [0, 1, 2, 3, 4, 5]
# pos = 7
# pos_new = pos % len(a)
# pos1 = -2
# pos1_new = pos1 % len(a)
# a = 5

def setup(matrx, rows, decor, gift, cookie, poss):
    for row in range(rows):
        row_data = input().split()
        for col in range(len(row_data)):
            if row_data[col] == "Y":
                poss = [row, col]
            elif row_data[col] == "D":
                decor.append([row, col])
            elif row_data[col] == "G":
                gift.append([row, col])
            elif row_data[col] == "C":
                cookie.append([row, col])
        matrx.append(row_data)
    return matrx, decor, gift, cookie, poss


def out_of_border_check(poss, matr):
    ro, co = poss
    ro = ro % len(matr)
    co = co % len(matr[0])
    # return ro, co
    print(ro, co)


decorations = []
gifts = []
cookies = []
matrix = []
position = []
m_rows, m_cols = [int(x) for x in input().split(", ")]
matrix, decorations, gifts, cookies, position = setup(matrix, m_rows, decorations, gifts, cookies, position)

position = [-1, -2]

out_of_border_check(position, matrix)


