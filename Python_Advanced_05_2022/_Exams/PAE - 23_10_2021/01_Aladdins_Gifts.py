from collections import deque


def product_check(item, produced, mat, mag):
    if item[1] <= produced <= item[2]:
        item[0] += 1
        mat.pop()
        mag.popleft()
    return item, produced, mat, mag


def magical_summation(mat, mag):
    summation = mat + mag
    if summation < min_limit:
        if summation % 2 == 0:
            summation = mat * 2 + mag * 3
        else:
            summation = summation * 2
    elif summation > max_limit:
        summation = summation / 2
    if min_limit <= summation <= max_limit:
        return [True, summation]
    else:
        return [False, summation]


min_limit = 100
max_limit = 499
gemstones = [0, 100, 199]
porcelains = [0, 200, 299]
gold = [0, 300, 399]
diamonds = [0, 400, 499]
materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

while True:
    if (not materials) or (not magics):
        break

    material = materials[-1]
    magic = magics[0]

    product = magical_summation(material, magic)
    if not product[0]:
        materials.pop()
        magics.popleft()
    if 100 <= product[1] <= 199:
        gemstones, product[1], materials, magics = product_check(gemstones, product[1], materials, magics)
        continue
    if 200 <= product[1] <= 299:
        porcelains, product[1], materials, magics = product_check(porcelains, product[1], materials, magics)
        continue
    if 300 <= product[1] <= 399:
        gold, product[1], materials, magics = product_check(gold, product[1], materials, magics)
        continue
    if 400 <= product[1] <= 499:
        diamonds, product[1], materials, magics = product_check(diamonds, product[1], materials, magics)
        continue

if (gemstones[0] > 0 and porcelains[0] > 0) or (gold[0] > 0 and diamonds[0] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magics:
    print(f"Magic left: {', '.join([str(x) for x in magics])}")

if diamonds[0] > 0:
    print(f"Diamond Jewellery: {diamonds[0]}")
if gemstones[0] > 0:
    print(f"Gemstone: {gemstones[0]}")
if gold[0] > 0:
    print(f"Gold: {gold[0]}")
if porcelains[0] > 0:
    print(f"Porcelain Sculpture: {porcelains[0]}")
