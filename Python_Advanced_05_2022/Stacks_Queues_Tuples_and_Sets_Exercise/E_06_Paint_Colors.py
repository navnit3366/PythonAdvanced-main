from collections import deque


def color_not_found(first, last, data):
    add_one = first[:-1]
    add_two = last[:-1]
    work_list = list(data)[1:-1]
    mid = len(work_list) // 2
    beginning = work_list[:mid]
    end = work_list[mid:]
    work_list = beginning
    if add_one:
        work_list.append(add_one)
    if add_two:
        work_list.append(add_two)
    work_list.extend(end)
    return deque(work_list)


def remove_secondary_bad_colors(fnd):
    if "orange" in fnd and not ("red" in fnd and "yellow" in fnd):
        fnd.remove("orange")
    if "purple" in fnd and not ("red" in fnd and "blue" in fnd):
        fnd.remove("purple")
    if "green" in fnd and not ("red" in fnd and "blue" in fnd):
        fnd.remove("green")
    return fnd


data = deque(input().split())

colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = ["orange", "purple", "green"]
found = []

while data:
    first = data[0]
    if len(data) == 1:
        last = ""
    else:
        last = data[-1]
    combo = first + last
    combo_two = last + first
    if combo in colors:
        found.append(combo)
        data.popleft()
        if data:
            data.pop()
    elif combo_two in colors:
        found.append(combo_two)
        data.popleft()
        if data:
            data.pop()
    else:
        data = color_not_found(first, last, data)

found = remove_secondary_bad_colors(found)

print(found)
