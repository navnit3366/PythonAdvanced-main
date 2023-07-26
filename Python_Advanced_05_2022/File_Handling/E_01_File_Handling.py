def replace_and_print(text):
    text = list(text.split(" "))
    for i in range(len(text)):
        word = list(text[i])
        for j in range(len(word)):
            # current = word[j]  # enable if you need for debugging purpose
            if word[j] in ["-", ",", ".", "!", "?"]:
                word[j] = "@"
        word = ''.join(word)
        text[i] = word
    print(" ".join(reversed(text)))

# Commented part of the code show a memory inefficient solution with ane big list containing all rows of the file.
# current solution is much better from this point.


# rows = []
line = []
try:
    # file = open("text.txt", 'r')
    # rows = file.read().split("\n")
    # file.close()
    row = 0
    file = open("text.txt", 'r')
    for line in file:
        if row % 2 == 0:
            replace_and_print(line.strip())
        row += 1
except FileNotFoundError:
    print("File not found or path is incorrect")

# Commented part of the code show a memory inefficient solution with a big list containing all rows of the file.
# current solution is much better from this point.
# for row_index in range(len(rows)):
#     if row_index % 2 == 0:
#         replace_and_print(rows[row_index])
