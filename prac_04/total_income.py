"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Asks for number of months and collects income and prints report through function"""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}:".format(month)))
        incomes.append(income)
    print_report(incomes)


def print_report(incomes):
    """Display income report for incomes over a given number of months."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()