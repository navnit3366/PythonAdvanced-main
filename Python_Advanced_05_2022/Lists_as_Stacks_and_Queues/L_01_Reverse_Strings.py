string = input()

stack = [char for char in string]

while stack:
    print(stack.pop(), end="")
