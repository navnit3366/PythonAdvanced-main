import re


def count_letters_and_punctuation_marks(string):
    # function return tuple with two values (number of letters, number_of_punctuation marks)
    pattern = r"[a-zA-Z]"
    number_of_letters = len(re.findall(pattern, string))
    number_of_punctuation_marks = len("".join(string.split(' '))) - number_of_letters
    return number_of_letters, number_of_punctuation_marks


line_count = 0
try:
    file = open("text.txt", "r")
    for line in file:
        line_count += 1
        punctuation_analysis = count_letters_and_punctuation_marks(line.strip())
        print(f"Line {line_count}: {line.strip()} ({punctuation_analysis[0]})({punctuation_analysis[1]})")
except FileNotFoundError:
    print("File not found or path is incorrect")
