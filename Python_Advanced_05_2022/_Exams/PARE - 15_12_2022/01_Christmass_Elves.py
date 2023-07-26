from collections import deque


def enough_energy(elf_energy, box_energy):
    if elf_energy >= box_energy:
        return True
    return False


def too_little_energy(elf_energy):
    if elf_energy < 5:
        return True
    return False


def work(the_elf, all_elfs, the_box, all_boxes, toys, the_energy, count):
    if count % 3 == 0 and count % 5 != 0:
        if the_elf >= the_box * 2:
            toys += 2
            all_boxes.pop()
            the_energy += the_box * 2
            all_elfs.append((all_elfs.popleft() - the_box * 2) + 1)
        else:
            elfs.append(elfs.popleft() * hot_choco_energy_multiplayer)
    if count % 3 == 0 and count % 5 == 0:
        if the_elf >= the_box * 2:
            all_boxes.pop()
            the_energy += the_box * 2
            all_elfs.append(all_elfs.popleft() - the_box * 2)
        else:
            elfs.append(elfs.popleft() * hot_choco_energy_multiplayer)
    if count % 5 == 0 and count % 3 != 0:
        if the_elf >= the_box:
            the_energy += the_box
            all_boxes.pop()
            all_elfs.append(all_elfs.popleft() - the_box)
    if count % 5 != 0 and count % 3 != 0:
        if the_elf >= the_box:
            toys += 1
            all_boxes.pop()
            the_energy += the_box
            all_elfs.append((all_elfs.popleft() - the_box) + 1)
        else:
            elfs.append(elfs.popleft())

    return toys, the_energy, all_elfs, all_boxes


elfs = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]
hot_choco_energy_multiplayer = 2
energy_used = 0
toys_made = 0
counter = 0
while True:
    if not elfs or not boxes:
        break
    elf = elfs[0]
    box = boxes[-1]
    if too_little_energy(elf):
        elfs.popleft()
        continue
    counter += 1
    if not enough_energy(elf, box):
        elfs.append(elfs.popleft() * hot_choco_energy_multiplayer)
        continue
    else:
        toys_made, energy_used, elfs, boxes = work(elf, elfs, box, boxes, toys_made, energy_used, counter)

    if not elfs or not boxes:
        break

print(f"Toys: {toys_made}")
print(f"Energy: {energy_used}")
if elfs:
    print(f"Elves left: {', '.join([str(x) for x in elfs])}")
if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")

