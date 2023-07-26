lines = int(input())
even = set()
odd = set()

for line in range(1, lines + 1):
    ascii_sum = 0
    word = input()
    for char in word:
        ascii_sum += ord(char)
    integer_divide = (ascii_sum // line)
    if integer_divide % 2 == 0:
        even.add(integer_divide)
    else:
        odd.add(integer_divide)

e_s = sum(even)
o_s = sum(odd)
if sum(even) > sum(odd):
    print(', '.join([str(x) for x in even.symmetric_difference(odd)]))
elif sum(even) < sum(odd):
    print(', '.join([str(x) for x in odd.difference(even)]))
else:
    print(', '.join([str(x) for x in even.union(odd)]))
