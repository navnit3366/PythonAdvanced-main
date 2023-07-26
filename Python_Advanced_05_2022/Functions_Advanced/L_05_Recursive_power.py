def recursive_power(val, power):
    if power == 0:
        return 1
    res = val * recursive_power(val, power - 1)
    return res


print(recursive_power(10, 100))