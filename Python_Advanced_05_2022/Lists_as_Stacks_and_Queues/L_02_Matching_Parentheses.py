string = input()

stack_of_indexes = []

for idx in range(len(string)):
    if string[idx] == "(":
        stack_of_indexes.append(idx)
    elif string[idx] == ")":
        end_of_substring = idx + 1
        start_of_substring = stack_of_indexes.pop()
        print(string[start_of_substring:end_of_substring])
