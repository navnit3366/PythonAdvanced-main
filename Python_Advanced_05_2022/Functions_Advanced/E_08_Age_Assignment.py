def age_assignment(*args, **kwargs):
    name_age_dict = {}
    result = ""
    for name in args:
        if name[0] in kwargs:
            age = kwargs[name[0]]
            if age not in name_age_dict:
                name_age_dict[age] = [name]
            else:
                name_age_dict[age].append(name)

    for k, v in sorted(name_age_dict.items(), key=lambda x: x[1]):
        for name in v:
            result += f"{name} is {k} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "POTER", "George", G=26, P=19))