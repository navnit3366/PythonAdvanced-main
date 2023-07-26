from collections import deque
from math import floor


input_string = deque([int(x) if x not in "+-*/" else x for x in input().split()])

operating_deque = deque()

while input_string:
    element = input_string.popleft()
    if str(element) not in "+-*/":
        operating_deque.append(element)
    else:
        if element == "+":
            result = operating_deque.popleft()
            while operating_deque:
                result += operating_deque.popleft()
            operating_deque.append(result)
        elif element == "-":
            result = operating_deque.popleft()
            while operating_deque:
                result -= operating_deque.popleft()
            operating_deque.append(result)
        elif element == "*":
            result = operating_deque.popleft()
            while operating_deque:
                result *= operating_deque.popleft()
            operating_deque.append(result)
        elif element == "/":
            result = operating_deque.popleft()
            while operating_deque:
                result /= operating_deque.popleft()
            operating_deque.append(floor(result))
print(*operating_deque)
