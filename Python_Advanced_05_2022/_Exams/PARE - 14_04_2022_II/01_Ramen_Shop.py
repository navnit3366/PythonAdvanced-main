from collections import deque

ramens = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while customers:
    if not ramens:
        break

    ramen = ramens[-1]
    customer = customers[0]

    if ramen == customer:
        ramens.pop()
        customers.popleft()
    elif ramen > customer:
        ramens[-1] -= customers.popleft()
    elif ramen < customer:
        customers[0] -= ramens.pop()

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print("Great job! You served all the customers.")
    if ramens:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramens])}")

