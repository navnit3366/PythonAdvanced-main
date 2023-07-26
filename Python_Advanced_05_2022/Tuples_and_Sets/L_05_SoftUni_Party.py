count = int(input())
vip = set()
regular = set()
for guest in range(count):
    code = input()
    if code[0].isdigit():
        vip.add(code)
    else:
        regular.add(code)
arrived = set()
arriving_code = input()
while arriving_code != "END":
    arrived.add(arriving_code)
    arriving_code = input()

# not_come_vip = vip.difference(arrived)
# not_come_regular = regular.difference(arrived)
# print(len(not_come_vip) + len(not_come_regular))

print(count - len(arrived))
[print(x) for x in sorted(vip.difference(arrived))]
[print(x) for x in sorted(regular.difference(arrived))]
