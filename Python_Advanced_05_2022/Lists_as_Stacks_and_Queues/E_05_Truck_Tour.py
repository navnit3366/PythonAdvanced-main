from collections import deque

pumps_list = deque()
pumps = int(input())
counter = 0
for pump in range(pumps):
    petrol, distance = [int(x) for x in input().split()]
    pumps_list.append((petrol, distance, counter))
    counter += 1

available_fuel = 0
for pump_ in range(len(pumps_list)):
    fail = False
    available_fuel = 0
    for current_pump_fuel, next_pump_distance, pump_index in pumps_list:
        available_fuel += current_pump_fuel
        if available_fuel >= next_pump_distance:
            available_fuel -= next_pump_distance
        else:
            fail = True
            break
    if fail:
        pumps_list.append(pumps_list.popleft())
    else:
        break
print(pumps_list[0][2])
