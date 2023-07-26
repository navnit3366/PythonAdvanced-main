a = [
    [1, 2, 3],
    [1, 3, 5],
    [1, 6, 7],
    ]
# cnt = 0
# for r in range(3):
#     a.append([])
#     for c in range(3):
#         cnt += 1
#         a[r].append("x")
print(a)
counter = 0
# for r in range(3):
#     for c in range(3):
#         if c % 3 == counter:
#             print(a[r][c])
#     counter += 1

z = all([a[ro][0] == a[0][0] for ro in range(len(a))])

print(z)
#
# for c in range(3):
#     for r in range(3):
#         print(a[r][c])
