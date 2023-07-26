def words_sorting(*words):
    string = []
    words_dict = {}
    sum_of_values = 0
    for word in words:
        value = sum([ord(char) for char in word])
        words_dict[word] = value
        sum_of_values += value
    if sum_of_values % 2 != 0:
        for word, value in sorted(words_dict.items(), key=lambda x: -x[1]):
            string.append(f"{word} - {value}")
    else:
        for word, value in sorted(words_dict.items(), key=lambda x: x[0]):
            string.append(f"{word} - {value}")

    return "\n".join(string)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
