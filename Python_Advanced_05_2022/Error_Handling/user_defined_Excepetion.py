class ValueCannotBePositive(Exception):
    """Number is below Zero"""
    pass


for i in range(-10, 15):
    num = i
    if num > 0:
        raise ValueCannotBePositive
    print(i)
