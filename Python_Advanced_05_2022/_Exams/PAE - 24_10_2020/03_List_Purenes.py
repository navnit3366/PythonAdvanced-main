from collections import deque
import sys


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    purenes = -sys.maxsize
    rotation = 0

    for i in range(k + 1):  # it's important to check last option too :P
        mid_sum = 0

        for j in range(len(numbers)):
            mid_sum += numbers[j] * j

        if mid_sum > purenes:
            purenes = mid_sum
            rotation = i

        numbers.rotate()

    return f"Best pureness {purenes} after {rotation} rotations"


test = ([-4, -3, -2, -6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
