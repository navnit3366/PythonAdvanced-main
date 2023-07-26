count = int(input())
names = set()

for name in range(count):
    names.add(input())

[print(x) for x in names]
