from collections import deque


def honey_calc(bee_val, symb, nec_val):
    if symb == "+":
        return bee_val+nec_val
    elif symb == "-":
        return bee_val-nec_val
    elif symb == "*":
        return bee_val*nec_val
    elif symb == "/":
        return bee_val/nec_val


working_bees = deque([int(x) for x in input().split()])
nectars = deque([int(x) for x in input().split()])
symbols = deque(input().split())

honey_produced = deque()

while working_bees:
    if not nectars:
        break
    current_bee = working_bees[0]
    current_nectar = nectars[-1]
    if current_nectar >= current_bee:
        nectar_value = nectars.pop()
        bee_value = working_bees.popleft()
        symbol = symbols.popleft()
        result = honey_calc(bee_value, symbol, nectar_value)
        honey_produced.append(abs(result))
    else:
         nectars.pop()

print(f"Total honey made: {sum(honey_produced)}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
