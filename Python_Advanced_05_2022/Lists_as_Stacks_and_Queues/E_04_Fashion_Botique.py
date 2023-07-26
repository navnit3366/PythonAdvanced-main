from collections import deque

clothes_in_the_box = deque([int(x) for x in input().split()])
rack_capacity = int(input())
used_racks = 0
current_rack_space = rack_capacity

while clothes_in_the_box:
    if clothes_in_the_box[-1] <= current_rack_space:
        current_rack_space -= clothes_in_the_box.pop()
        if current_rack_space == 0:
            used_racks += 1
            current_rack_space = rack_capacity
    else:
        used_racks += 1
        current_rack_space = rack_capacity
        current_rack_space -= clothes_in_the_box.pop()

if current_rack_space > 0 and current_rack_space != rack_capacity:
    used_racks += 1

print(used_racks)