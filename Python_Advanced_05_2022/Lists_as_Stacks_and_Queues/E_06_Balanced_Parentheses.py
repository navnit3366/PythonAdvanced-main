
string = list(input())
# print(string)
stack = []
open_parentheses = []
if len(string) % 2 == 0:
    for char in string:
        if char in "{([":
            open_parentheses.append(char)

#  Do it with pairs dict !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        elif char == "}" and open_parentheses[-1][0] == "{":
            open_parentheses.pop()
        elif char == ")" and open_parentheses[-1][0] == "(":
            open_parentheses.pop()
        elif char == "]" and open_parentheses[-1][0] == "[":
            open_parentheses.pop()

    if len(open_parentheses) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
