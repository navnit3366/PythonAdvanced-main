from collections import deque


def reload_check(cntr, available_b, brl):
    if cntr == 0 and available_b > 0:
        print(f"Reloading!")
        return brl
    else:
        return cntr


bullet_price = int(input())
barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
prize = int(input())

counter = barrel
expense = 0
while bullets:
    counter -= 1
    expense += bullet_price
    if bullets[-1] <= locks[0]:
        bullets.pop()
        locks.popleft()
        print(f"Bang!")
        if not locks:
            counter = reload_check(counter, len(bullets), barrel)
            break
    else:
        bullets.pop()
        print(f"Ping!")
    counter = reload_check(counter, len(bullets), barrel)

if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${prize - expense}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
