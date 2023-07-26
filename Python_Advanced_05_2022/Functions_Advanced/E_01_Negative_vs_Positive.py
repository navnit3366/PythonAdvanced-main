def separator(args):
    positive_sum = sum([x for x in args if x > 0])
    negative_sum = sum([x for x in args if x < 0])
    print(f"{negative_sum}")
    print(f"{positive_sum}")
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


separator([int(x) for x in (input().split())])
