#  TODO To do thursday night
# Set up class file with def for init and str and like fuel and drive we need to grab this data out as we want it


# In running code, set up def main with the while loop
# Set up def in the class file to be placed in the def main file
from prac_06.car import Car
MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(100,name)
    print(car)
    print(MENU)
    choice = input('Enter your choice: ').upper()
    while choice != 'Q':
        if choice == 'D':
            pass
        elif choice == 'R':
            refuel = int(input('How many units of fuel do you want to add to the car? '))
            if refuel < 0:
                print('Fuel amount must be >= 0')
                refuel = int(input('How many units of fuel do you want to add to the car? '))
            car.add_fuel(refuel)
            print('Added {} units of fuel'.format(refuel))
        else:
            print('Invalid choice')
            print(car)
            print(MENU)
            choice = input('Enter your choice: ').upper()
    print("Good bye {}'s driver".format(name))


main()