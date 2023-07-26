def even_odd_filter(**args):

    def sort_a_dict(dictio):
        sorted_dictionary = {}
        for k_ey, value in sorted(dictio.items(), key=lambda x: -len(x[1])):
            sorted_dictionary[k_ey] = value
        return sorted_dictionary

    filtered_dict = {}
    for k_ey, values in args.items():
        if k_ey == "even":
            filtered_dict[k_ey] = [x for x in values if x % 2 == 0]
        else:
            filtered_dict[k_ey] = [x for x in values if x % 2 != 0]

    return sort_a_dict(filtered_dict)


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
