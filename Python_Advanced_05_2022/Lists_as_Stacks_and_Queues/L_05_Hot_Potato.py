from collections import deque

kids_queue = deque()

data = [kids_queue.append(kid) for kid in input().split()]  #
toss_count = int(input())  #
while len(kids_queue) != 1:
    for toss in range(1, toss_count+1):
        if toss < toss_count:
            kid = kids_queue.popleft()
            kids_queue.append(kid)
        else:
            print(f"Removed {kids_queue.popleft()}")
        if len(kids_queue) == 1:
            break
print(f"Last is {kids_queue[0]}")
