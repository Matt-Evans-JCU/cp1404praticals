number_string_occurrence = {}
text = input("Text: ")
strings = text.split()
for string in strings:
    try:
        number_string_occurrence[string] += 1
    except KeyError:
        number_string_occurrence[string] = 1



for string_name, string_count in number_string_occurrence.items():
    print('{} : {}'.format(string_name,string_count))
