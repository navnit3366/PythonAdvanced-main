from collections import deque


effects = deque([int(x) for x in input().split(',')])  # first
casings = [int(x) for x in input().split(',')]  # last

datura = []
cherry = []
smoke = []

while True:
    effect = effects[0]
    casing = casings[-1]
    mix = effect + casing
    if mix == 40:
        datura.append(mix)
        effects.popleft()
        casings.pop()
    elif mix == 60:
        cherry.append(mix)
        effects.popleft()
        casings.pop()
    elif mix == 120:
        smoke.append(mix)
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5
    if not effects:
        break
    if not casings:
        break
    if len(datura) >= 3 and len(cherry) >= 3 and len(smoke) >= 3:
        break


if len(datura) >= 3 and len(cherry) >= 3 and len(smoke) >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print("Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")
else:
    print("Bomb Casings: empty")


print(f"Cherry Bombs: {len(cherry)}")
print(f"Datura Bombs: {len(datura)}")
print(f"Smoke Decoy Bombs: {len(smoke)}")






