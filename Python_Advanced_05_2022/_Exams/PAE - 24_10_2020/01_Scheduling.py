from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
index = int(input())

max_val = jobs[index]
current = 0
counter = 0
nn = 1000

while current <= max_val and nn > 0:
    current = min(jobs)
    jobs.remove(current)
    counter += current
    nn = jobs.count(max_val)
print(counter)
