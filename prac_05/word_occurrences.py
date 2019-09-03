number_string_occurrence = {}
text = input("Text: ")
strings = text.split()
max_string_length = 0

for string in strings:
    number_string_occurrence[string] = number_string_occurrence.get(string, 0) + 1
    if len(string) > max_string_length:
        max_string_length = len(string)

sorted_strings = sorted(number_string_occurrence)

for string in sorted_strings:
    print('{:{}} : {}'.format(string, max_string_length, number_string_occurrence[string]))
