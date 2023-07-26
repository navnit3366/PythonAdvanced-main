string = input()
char_count_dict = {}

for char in string:
    if char not in char_count_dict:
        char_count_dict[char] = 1
    else:
        char_count_dict[char] += 1

for char, count in sorted(char_count_dict.items()):
    print(f"{char}: {count} time/s")
