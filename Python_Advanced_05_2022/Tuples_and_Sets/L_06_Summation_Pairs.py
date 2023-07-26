numbers = [int(x) for x in input().split()]
target = int(input())
target_pairs = set()
counter = 0
for first in range(len(numbers)-1):
    for second in range(first+1, len(numbers)):
        counter += 1
        f = numbers[first]
        s = numbers[second]
        if numbers[first] + numbers[second] == target:
            print(f"{numbers[first]} + {numbers[second]} = {target}")
            if (numbers[first], numbers[second]) not in target_pairs:
                target_pairs.add((numbers[first], numbers[second]))

print(f"Iterations done: {counter}")

[print(x) for x in target_pairs]
