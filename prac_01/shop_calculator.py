""" 
Shopping Calculator
Pseudo:
Ask the user how many they have
Ask for the prices for each one
Calculate the total
Check if discount is possible and add if needed
print total cost
"""


TOTAL = 0
number_items = int(input('How many items do you have: '))
while number_items < 0:
    print('Invalid number of items!')
    number_items = int(input('How many items do you have: '))
for i in range(1, number_items + 1):
    cost_of_item = float(input('Price of item: '))
    TOTAL += cost_of_item
if TOTAL > 100:
    TOTAL *= .9
# print('Total price for %d items is %f' % number_items % TOTAL) %d only works for one insertable
print('Total price for {} item is ${:.2f}'.format(number_items, TOTAL))
