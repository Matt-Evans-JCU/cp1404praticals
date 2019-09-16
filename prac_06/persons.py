from operator import attrgetter

from prac_06.person import Person


def main():
    persons = []
    first_name = input('What is your first name? ')
    while first_name != '':
        last_name = input('What is your last name? ')
        age = int(input('What is your age? '))
        person = Person(first_name, last_name, age)
        persons.append(person)
        first_name = input('What is your first name? ')
    # For quicker use
    persons.append(Person('Bob', 'Jones', 68))
    persons.append((Person('Jane', 'Coleman', 45)))
    persons.sort(key=attrgetter('age'))
    for person in persons:
        print(person)
    persons_detail = []
    # Only pick first name
    person_detail = input("Who's details to you want ")
    while person_detail != '':
        persons_detail.append(person_detail)
        person_detail = input("Who's details to you want ")
    for person in persons:  # TODO: Can use an and to check mulitple fields or an 'or' if needed
        if person.first_name in persons_detail:
            print(person)


main()
