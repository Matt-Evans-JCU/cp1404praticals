from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    menu = """q)uit, c)hoose taxi, d)rive"""
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'C':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):   # The price_per_km in example 1.20 not 1.23
                print('{} - {}'.format(i,taxi))
            current_taxi = int(input('Choose taxi: '))
            print('Bill to date: ${:.2f}'.format(bill))
        if choice == 'D':
            drive_distance = int(input('Drive how far? '))
            taxis[current_taxi].drive(drive_distance)  # This updates self.current_fare_distance for driven distance
            cost_of_trip = taxis[current_taxi].get_fare()
            print('Your {} trip cost you ${:.2f}'.format(taxis[current_taxi].name,cost_of_trip))
            bill += cost_of_trip
            print('Bill to date: ${:.2f}'.format(bill))
        menu = """q)uit, c)hoose taxi, d)rive"""
        choice = input('>>> ').upper()
    print('Total trip cost: ${:.2f}'.format(bill))
    print('Taxis are now:')
    for i, taxi in enumerate(taxis):  # The price_per_km in example 1.20 not 1.23
        print('{} - {}'.format(i, taxi))


main()