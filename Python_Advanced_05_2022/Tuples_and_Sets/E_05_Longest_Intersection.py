import copy

lines = int(input())
longest_intersection = []

for line in range(lines):
    sets = [x.split(",") for x in input().split("-")]
    r1 = [int(x) for x in sets[0]]
    r2 = [int(x) for x in sets[1]]
    # for i in range(len(sets)):
    #     for j in range(len(sets[i])):
    #         sets[i][j] = int(sets[i][j])
    range_1 = set([i for i in range(r1[0], r1[1]+1)])
    range_2 = set([j for j in range(r2[0], r2[1]+1)])
    intersection = range_1.intersection(range_2)
    if len(intersection) > len(longest_intersection):
        longest_intersection = copy.deepcopy(intersection)
print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length "
      f"{len(longest_intersection)}")
