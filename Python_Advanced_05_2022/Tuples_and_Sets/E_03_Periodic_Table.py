lines = int(input())

set_of_compounds = set()

for line in range(lines):
    compounds = input().split()
    for compound in compounds:
        set_of_compounds.add(compound)

[print(x) for x in set_of_compounds]