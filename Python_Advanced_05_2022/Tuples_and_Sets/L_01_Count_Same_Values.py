floating_numbers = tuple([float(x) for x in input().split()])

unique_numbers = []
# it's not a good idea to use set() to limit unique_numbers because it's unordered

for num in floating_numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

for num in unique_numbers:
    print(f"{num} - {floating_numbers.count(num)} times")

# List comprehension to limit unique nums
# am = []
# am = [x for x in floating_numbers if x not in am]
# print(am)
