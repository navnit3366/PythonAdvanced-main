list_of_numbers_working_as_stack = [int(num) for num in input().split()]
while list_of_numbers_working_as_stack:
    print(list_of_numbers_working_as_stack.pop(), end=" ")
