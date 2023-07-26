def start_spring(**kwargs):
    output_string = ""
    by_type_dict = {}

    for keys, values in kwargs.items():
        if values not in by_type_dict:
            by_type_dict[values] = []
        by_type_dict[values].append(keys)

    for keys, values in sorted(by_type_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        output_string += f"{keys}:\n"
        for value in sorted(values):
            output_string += f"-{value}\n"

    return output_string


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))



