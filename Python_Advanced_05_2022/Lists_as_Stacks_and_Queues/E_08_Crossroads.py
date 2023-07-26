from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
command = input()
while command != "END":
    cars.append(command)
    command = input()

timer = 0
flag = True
total_cars_passed = 0

while cars:
    if cars[0] == "green":
        timer = 0
        current_car = cars.popleft()
    if timer <= green_light:
        if len(cars) > 0:
            current_car = cars.popleft()
        else:
            break
        for char in current_car:
            timer += 1
            if timer > (green_light + free_window):
                print(f"A crash happened!")
                print(f"{current_car} was hit at {char}.")
                flag = False
                break
        total_cars_passed += 1
    else:
        break
    if not flag:
        break

if flag:
    print(f"Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
