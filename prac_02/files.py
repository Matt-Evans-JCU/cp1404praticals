name = input("What is your name: ")
output_name = open("data.txt", 'w')
print(name, file= output_name)
output_name.close()

input_name = open("data.txt", 'r')
print("Your name is {}".format(input_name.readline()))
input_name.close()
input_numbers = open("numbers.txt",'r')
number_1 = int(input_numbers.readline())
number_two = int(input_numbers.readline())
total = number_1 + number_two
# print(numbers[0])
# print(numbers[1])
print(number_1)
print(number_two)
print(total)
input_numbers.close()

in_file_numbers = open("numbers.txt", 'r')  #input
total = 0
for line in in_file_numbers:
    number = int(line.strip())
    total += number
print("The total is {}".format(total))
in_file_numbers.close()