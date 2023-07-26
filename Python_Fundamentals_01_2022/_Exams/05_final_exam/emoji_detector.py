import re

string = input()
cool_threshold = 1
cool_list = []
emoji_list = []

for character in string:
    if character.isdigit():
        cool_threshold *= int(character)
print(f"Cool threshold: {cool_threshold}")

pattern = r"(?P<symbols>(::|\*\*))(?P<emoji>([A-Z][a-z]{2,}))(?P=symbols)"

result = [obj.groupdict() for obj in re.finditer(pattern, string)]
for dict in result:
    emoji_list.append(dict["emoji"])
    coolness = 0
    for character in dict["emoji"]:
        coolness += ord(character)
    if coolness >= cool_threshold:
        emo = dict["symbols"] + dict["emoji"] + dict["symbols"]
        cool_list.append(emo)
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
for emoji in cool_list:
    print(f"{emoji}")