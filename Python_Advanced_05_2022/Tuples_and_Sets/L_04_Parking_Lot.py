records = int(input())
cars_plates = set()
for car in range(records):
    command, plate = input().split(", ")
    if command == "IN":
        cars_plates.add(plate)
    else:
        cars_plates.remove(plate)

if not cars_plates:
    print(f"Parking Lot is Empty")
else:
    [print(plate) for plate in cars_plates]
