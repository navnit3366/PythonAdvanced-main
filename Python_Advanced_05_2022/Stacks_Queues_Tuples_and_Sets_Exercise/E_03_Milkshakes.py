from collections import deque


chocolate = deque([int(x) for x in input().split(", ")])
milk = deque([int(x) for x in input().split(", ")])

milkshake_counter = 0

while chocolate:
    if chocolate[-1] <= 0:
        chocolate.pop()
    if milk[0] <= 0:
        milk.popleft()
    if not chocolate or not milk:
        break
    current_chocolate = chocolate.pop()
    current_milk = milk.popleft()
    if current_chocolate == current_milk:
        milkshake_counter += 1
    else:
        milk.append(current_milk)
        new_choco = current_chocolate - 5
        chocolate.append(new_choco)
    if milkshake_counter == 5:
        break
    if not milk:
        break
    if not chocolate:
        break

if milkshake_counter == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print(f"Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print(f"Milk: empty")
    
