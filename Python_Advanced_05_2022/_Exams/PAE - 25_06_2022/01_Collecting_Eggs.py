from collections import deque

eggs_sizes = deque([int(x) for x in input().split(", ")])
paper_sizes = deque([int(x) for x in input().split(", ")])
boxes = []


while eggs_sizes:
    if not paper_sizes:
        break

    egg = eggs_sizes[0]
    paper = paper_sizes[-1]

    if egg <= 0:
        eggs_sizes.popleft()
        continue
    elif egg == 13:
        eggs_sizes.popleft()
        front = paper_sizes.pop()
        end = paper_sizes.popleft()
        paper_sizes.appendleft(front)
        paper_sizes.append(end)
        continue

    value = egg + paper
    if value <= 50:
        boxes.append(value)
        eggs_sizes.popleft()
        paper_sizes.pop()
    else:
        eggs_sizes.popleft()
        paper_sizes.pop()

if boxes:
    print(f"Great! You filled {len(boxes)} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_sizes:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_sizes])}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper_sizes])}")
