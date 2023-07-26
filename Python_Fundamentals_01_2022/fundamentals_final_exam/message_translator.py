import re
number_of_commands = int(input())

pattern = r"\!(?P<command>[A-Z][a-z]{2,})\!\:\[(?P<string>[A-Za-z]{8,})\]"

for line in range(number_of_commands):
    command = input()
    result = [obj.groupdict() for obj in re.finditer(pattern, command)]
    if result:
        command = result[0]["command"]
        string = result[0]["string"]
        translation = []
        for char in string:
            translation.append(str(ord(char)))
        # print(translation)
        print(f"{command}: {(' ').join(translation)}")
    else:
        print(f"The message is invalid")


