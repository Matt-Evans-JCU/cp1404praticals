number_string_occurrence = {}
text = input("Text: ")
strings = text.split()
for string in strings:
    number_string_occurrence[string] = number_string_occurrence.get(string,0)+1

sorted_strings= sorted(number_string_occurrence)

for string in sorted_strings:
    print('{} : {}'.format(string,number_string_occurrence[string]))