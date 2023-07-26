stack = []

command_lines = int(input())
for com in range(command_lines):
    input_command = [int(num) for num in input().split()]
    command = input_command[0]
    if command == 1:
        stack.append(input_command[1])
    elif command == 2:
        if len(stack) > 0:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))

print_list = []

while stack:
    print_list.append(str(stack.pop()))
print(", ".join(print_list))

# print(*[stack.pop() for x in range(len(stack))], sep=", ")
