lines = int(input())
names = set()

for line in range(lines):
    names.add(input())

[print(element) for element in names]
