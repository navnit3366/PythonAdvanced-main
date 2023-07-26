def output_values(key, value):
    return f"{key} - {value}\n"


def words_sorting(*words):
    words_with_ascii_sum = {}
    values_sum = 0
    output_string = ""
    for word in words:
        ascii_sum = sum([ord(char) for char in word])
        values_sum += ascii_sum
        words_with_ascii_sum[word] = ascii_sum

    if values_sum % 2 == 0:
        for k, v in sorted(words_with_ascii_sum.items()):
            output_string += output_values(k, v)

    else:
        for k, v in sorted(words_with_ascii_sum.items(), reverse=True):
            output_string += output_values(k, v)

    return output_string


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
