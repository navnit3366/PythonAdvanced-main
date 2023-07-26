def operate(operator, *args):
    def plus(arguments):
        return sum(arguments)

    def minus(arguments):
        res = arguments[0]
        for i in range(1, len(arguments)):
            res -= arguments[i]
        return res

    def multiply(arguments):
        res = 1
        for val in arguments:
            res *= val
        return res

    def divide(arguments):
        res = arguments[0]
        for i in range(1, len(arguments)):
            val = arguments[i]
            res /= arguments[i]
        return res

    if operator == "+":
        return plus(args)
    elif operator == "-":
        return minus(args)
    elif operator == "*":
        return multiply(args)
    elif operator == "/":
        return divide(args)


# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("-", 1, 2, 3))
print(operate("/", 10, 2, 2))