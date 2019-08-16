from math import sqrt

upper_bound = int(input('What do you wish to be the upper bound: '))
lower_bound = int(input('What do you wish to be the lower bound: '))
difference = upper_bound - lower_bound
while difference <= 0:
    print('Invalid inputs upper bound must be larger than lower bound')
    upper_bound = int(input('What do you wish to be the upper bound: '))
    lower_bound = int(input('What do you wish to be the lower bound: '))
    difference = upper_bound - lower_bound
menu = """(E)ven
(O)dd
(S)quare
(Q)uit"""
print(menu)
choice = input('What choice do you wish to in act: ').upper()
while choice != "Q":
    if choice == "E":
        for i in range(lower_bound, upper_bound+1, 1):
            if (i % 2) == 0:
                print(i, end=' ')
            else:
                pass
        print()
    elif choice == "O":
        for i in range(lower_bound, upper_bound + 1, 1):
            if (i % 2) != 0:
                print(i, end=' ')
            else:
                pass
        print()
    elif choice == "S":
        for i in range(lower_bound, upper_bound+1, 1):
            print(i*i, end=' ')
        print()
    else:
        print("Invalid Letter Try Again")
    print(menu)
    choice = input('What choice do you wish to in act: ').upper()
print("Session Finished")