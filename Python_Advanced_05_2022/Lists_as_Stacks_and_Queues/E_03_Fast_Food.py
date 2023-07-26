from collections import deque

available_food = int(input())
queue = deque([int(x) for x in input().split()])

print(max(queue))


while queue:
    if queue[0] <= available_food:
        available_food -= queue.popleft()
    else:
        break

if len(queue) == 0:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in queue])}")
