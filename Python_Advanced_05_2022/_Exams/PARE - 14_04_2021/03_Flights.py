def flights(*data):
    destination_filtered = {}
    if data:
        for i in range(len(data)):
            data_i = data[i]
            if data[i] == "Finish":
                break
            if i % 2 != 0:
                if data[i - 1] not in destination_filtered:
                    destination_filtered[data[i - 1]] = 0
                destination_filtered[data[i - 1]] += data[i]
    else:
        pass
    return destination_filtered


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
