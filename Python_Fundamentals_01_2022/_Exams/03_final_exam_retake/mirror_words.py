import re
string = input()
mirror_pairs = {}
any_word_pairs = {}
final = []
pattern = r"(?P<symbol>(@|#))(?P<first>[A-Za-z]{3,})(?P=symbol)(?P=symbol)(?P<second>[A-Za-z]{3,})(?P=symbol)"
result = [obj.groupdict() for obj in re.finditer(pattern, string)]
for dict in result:
    any_word_pairs[dict["first"]] = dict["second"]
    if dict["first"] == dict["second"][::-1]:
        mirror_pairs[dict["first"]] = dict["second"]
if len(any_word_pairs) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(any_word_pairs)} word pairs found!")
if len(mirror_pairs) == 0:
    print(f"No mirror words!")
else:
    # print(f"{len(mirror_pairs)} word pairs found!")
    print(f"The mirror words are:")
    for first, second in mirror_pairs.items():
        # str = first + " <=> " + second
        final.append(first + " <=> " + second)
    print(", ".join(final))