your_cars = int(input())
garage = {}

for car_ in range(your_cars):
    this_car = input().split("|")
    model = this_car[0]
    mileage = int(this_car[1])
    fuel = int(this_car[2])
    garage[model] = [mileage, fuel]

command = input()
while command != "Stop":
    s_command = command.split(" : ")
    this_command = s_command[0]
    if this_command == "Drive":
        car = s_command[1]
        distance = int(s_command[2])
        needed_fuel = int(s_command[3])
        garage_distance = garage[car][0]
        garage_fuel = garage[car][1]
        if garage_fuel < needed_fuel:
            print(f"Not enough fuel to make that ride")
        else:
            garage[car][0] += distance
            garage[car][1] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if garage[car][0] >= 100000:
            del garage[car]
            print(f"Time to sell the {car}!")
    elif this_command == "Refuel":
        car = s_command[1]
        new_fuel = int(s_command[2])
        garage_fuel = garage[car][1]
        if (new_fuel + garage_fuel) > 75:
            refill = (75 - garage_fuel)
        else:
            refill = new_fuel
        garage[car][1] += refill
        print(f"{car} refueled with {refill} liters")
    elif this_command == "Revert":
        car = s_command[1]
        decrease_of_km = int(s_command[2])
        garage[car][0] -= decrease_of_km
        if garage[car][0] < 10000:
            garage[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {decrease_of_km} kilometers")
    command = input()

for car, data in garage.items():
    print(f"{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")


