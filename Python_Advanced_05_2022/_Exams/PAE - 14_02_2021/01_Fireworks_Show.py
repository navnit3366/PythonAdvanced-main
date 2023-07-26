from collections import deque

f_effects = deque([int(x) for x in input().split(", ")])
e_power = [int(x) for x in input().split(", ")]

palm = 0
willow = 0
cross = 0

perfect = False

while not perfect:
    if not f_effects:
        break
    if not e_power:
        break

    no_fireworks = True
    firework = f_effects[0]
    power = e_power[-1]
    value = firework + power

    if power <= 0:
        e_power.pop()
        continue
    if firework <= 0:
        f_effects.popleft()
        continue

    if not f_effects:
        break
    if not e_power:
        break

    if value % 3 == 0 and value % 5 != 0:
        palm += 1
        e_power.pop()
        f_effects.popleft()
        no_fireworks = False

    if value % 3 != 0 and value % 5 == 0:
        willow += 1
        e_power.pop()
        f_effects.popleft()
        no_fireworks = False

    if value % 3 == 0 and value % 5 == 0:
        cross += 1
        e_power.pop()
        f_effects.popleft()
        no_fireworks = False

    if no_fireworks:
        f_effects.append(f_effects.popleft() - 1)

    if palm >= 3 and willow >= 3 and cross >= 3:
        perfect = True

if perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if f_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in f_effects])}")
if e_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in e_power])}")

print(f"Palm Fireworks: {palm}")

print(f"Willow Fireworks: {willow}")

print(f"Crossette Fireworks: {cross}")
