op = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for num in range(0, 4, 1):
    print(f"pos{num}")
    for i in range(len(op)):
        if (i-num) % 4 == 0:
            print(op[i])



# a = ["a", "b", "c", "d", "e", "f", "g", "h", "k", "l"]
#
# for i in range(len(a)):
#     if (i-1) % 4 == 0:
#         print(a[i])

#  pos 0
# print("pos0")
# op = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# for i in range(len(op)):
#     if (i) % 4 == 0:
#         print(op[i])
# #  pos 1
# print("pos1")
# for i in range(len(op)):
#     if (i-1) % 4 == 0:
#         print(op[i])
# #  pos 2
# print("pos2")
# for i in range(len(op)):
#     if (i-2) % 4 == 0:
#         print(op[i])
# print("pos3")
# for i in range(len(op)):
#     if (i-3) % 4 == 0:
#         print(op[i])
