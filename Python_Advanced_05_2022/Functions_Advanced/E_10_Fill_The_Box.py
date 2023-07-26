from collections import deque


def fill_the_box(width, length, height, *commands):
    size = width * height * length
    comm = deque([x for x in commands])
    command = comm.popleft()
    result = ""
    there_is_more_space = True
    while command != "Finish":
        if size - command <= 0:
            rest = abs(size - command)
            for i in comm:
                if i != "Finish":
                    rest += i
            result = f"No more free space! You have {rest} more cubes."
            there_is_more_space = False
            break
        else:
            size -= command
        command = comm.popleft()

    if there_is_more_space:
        result = f"There is free space in the box. You could put {size} more cubes."
    return result


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
