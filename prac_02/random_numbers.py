import random

print(random.randint(5, 20))  # line 1
# On line 1 I saw 17
# The lowest number possible to see is 5 and the largest number is 20
print(random.randrange(3, 10, 2))  # line 2
# On line 2 I saw 9
# The lowest number possible to see is 5 and the largest number is 9
# Note 4 is not possible as the random range only picks from steps of 2 from 3
print(random.uniform(2.5, 5.5))  # line 3
# On line 3 I saw 5.419875291293577
# The lowest number possible to see is 2.500000001 and the largest number is 5.4999999999
