"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = fahrenheit_calculation(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = celsius_calculation(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_calculation(celsius):
    return celsius * 9.0 / 5 + 32


def celsius_calculation(fahrenheit):
    return (fahrenheit - 32) / 9.0 * 5


main()
