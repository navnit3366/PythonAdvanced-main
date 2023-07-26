from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

waste = 0
while bottles:
    current_bottle = bottles.pop()
    current_cup = cups[0]
    if current_cup > current_bottle:
        cups[0] -= current_bottle

    if current_cup <= current_bottle:
        current_bottle -= current_cup
        waste += current_bottle
        cups.popleft()
    if len(cups) == 0:
        break

if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")

if not bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {waste}")
