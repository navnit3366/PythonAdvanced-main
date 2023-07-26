from collections import deque


def add_numbers(numbers, in_sequence):
    for number in numbers:
        if in_sequence == "First":
            first_sequence.add(number)
        else:
            second_sequence.add(number)


def remove_numbers(numbers, in_sequence):
    for number in numbers:
        if in_sequence == "First" and number in first_sequence:
            first_sequence.remove(number)
        elif in_sequence == "Second" and number in second_sequence:
            second_sequence.remove(number)


first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(y) for y in input().split()])

input_lines = int(input())

for line in range(input_lines):
    input_line = deque(input().split())
    command = input_line.popleft()
    sequence = input_line.popleft()
    new_set = set([int(x) for x in input_line])

    if command == "Add":
        add_numbers(new_set, sequence)
    elif command == "Remove":
        remove_numbers(new_set, sequence)
    elif command == "Check":
        if second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence):
            print("True")
        else:
            print("False")

print(", ".join([str(x) for x in sorted(first_sequence)]))
print(", ".join([str(x) for x in sorted(second_sequence)]))
