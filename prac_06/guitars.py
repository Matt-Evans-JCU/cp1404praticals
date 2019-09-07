from prac_06.guitar import Guitar


def main():
    guitars = []
    name = input('Guitar name: ')
    while not name == '':
        year = int(input('Year: '))
        cost = float(input('Cost: $'))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print('{} ({}) : ${:.2f} added.'.format(name, year, cost))
        name = input('Guitar name: ')
    # To make quicker
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    for i, guitar in enumerate(guitars):
        vintage_string = ''
        if guitar.is_vintage():
            vintage_string = '(vintage)'
        print(
            "Guitar {}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {}".format(i + 1, vintage_string,
                                                                                                  guitar=guitar))

main()
