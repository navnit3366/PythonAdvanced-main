from collections import deque

orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
made = 0

while True:
    if not orders:
        break
    if not employees:
        break

    order = orders[0]
    employer = employees[-1]

    if order <= 0:
        orders.popleft()
        continue

    if order < 11:
        if order <= employer:
            made += orders.popleft()
            employees.pop()
        else:
            made += employer
            orders[0] -= employees.pop()
    else:
        orders.popleft()

if not orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {made}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")
