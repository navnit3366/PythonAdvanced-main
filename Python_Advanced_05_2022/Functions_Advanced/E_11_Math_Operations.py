def math_operations(*args, **kwargs):
    res = ""

    def every_fourth(num):
        result = []
        for i in range(len(args)):
            if (i - num) % 4 == 0:
                result.append(args[i])
        return result

    for operation in kwargs:
        if operation == "a":
            n = 0
            values_to_operate = every_fourth(n)
            for val in values_to_operate:
                kwargs[operation] += val
        if operation == "s":
            n = 1
            values_to_operate = every_fourth(n)
            for val in values_to_operate:
                kwargs[operation] -= val
        if operation == "d":
            n = 2
            values_to_operate = every_fourth(n)
            for val in values_to_operate:
                if val != 0:
                    kwargs[operation] /= val
        if operation == "m":
            n = 3
            values_to_operate = every_fourth(n)
            for val in values_to_operate:
                kwargs[operation] *= val
    for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        res += f"{k}: {v:.1f}\n"
    return res


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
