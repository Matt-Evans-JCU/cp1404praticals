number_string_occurrence = {}
text = input("Text: ")
strings = text.split()
for string in strings:
    number_string_occurrence[string] = number_string_occurrence.get(string,0)+1



for string_name, string_count in number_string_occurrence.items():
    print('{} : {}'.format(string_name,string_count))
