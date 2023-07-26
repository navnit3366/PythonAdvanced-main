from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0
while True:
    if not females or not males:
        break
    female = females[0]
    male = males[-1]
    if male % 25 == 0 and male != 0:
        males.pop()
        males.pop()
        continue
    if female % 25 == 0 and female != 0:
        females.popleft()
        females.popleft()
        continue

    if male <= 0:
        males.pop()
        continue
    if female <= 0:
        females.popleft()
        continue
    if male == female:
        matches += 1
        males.pop()
        females.popleft()
    else:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(males[x]) for x in range(-1, -len(males)-1, -1)])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
