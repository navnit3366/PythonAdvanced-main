def concatenate(*args, **kwargs):
    string = ""
    for _ in args:
        string += _

    for k, v in kwargs.items():
        string = string.replace(k, v)
    return string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))