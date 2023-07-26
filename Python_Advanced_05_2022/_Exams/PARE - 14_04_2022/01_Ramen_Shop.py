from collections import deque

bowls = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while all([bowls, customers]):
    current_bowl = bowls[-1]
    current_customer = customers[0]
    if current_bowl == current_customer:
        bowls.pop()
        customers.popleft()
    elif current_bowl > current_customer:
        bowls[-1] -= customers.popleft()
    elif current_bowl < current_customer:
        customers[0] -= bowls.pop()


if not customers:
    print(f"Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls])}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
