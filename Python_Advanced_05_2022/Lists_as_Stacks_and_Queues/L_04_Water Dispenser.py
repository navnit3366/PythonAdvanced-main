from collections import deque

watter = int(input())
name = input()
peoples_queue = deque()

while name != "Start":
    peoples_queue.append(name)
    name = input()

command = input()
while command != "End":
    command = command.split()
    if command[0].isnumeric():
        litters_needed = int(command[0])
        if watter >= litters_needed:
            watter -= litters_needed
            print(f"{peoples_queue.popleft()} got water" )
        else:
            print(f"{peoples_queue[0]} must wait")
    elif command[0] == "refill":
        watter += int(command[1])
    command = input()
print(f"{watter} liters left")
