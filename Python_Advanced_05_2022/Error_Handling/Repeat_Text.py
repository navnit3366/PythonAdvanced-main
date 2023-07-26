try:
    message = input()
    times = int(input())
    print(times * message)
except ValueError:
    print(f"Variable 'times' must be integer")


