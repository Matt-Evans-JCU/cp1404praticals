import random
LOWER_LIMIT = 1
UPPER_LIMIT = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    for i in range(1,number_of_picks+1):
        quick_pick_numbers = []
        for j in range(1, 7):
            random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT + 1)
            while random_number in quick_pick_numbers:
                random_number = random.randint(1, 100)
            quick_pick_numbers.append(random_number)
        quick_pick_numbers = sorted(quick_pick_numbers)
        print('{0:>2d} {1:>2d} {2:>2d} {3:>2d} {4:>2d} {5:>2d}'.format(quick_pick_numbers[0],quick_pick_numbers[1],quick_pick_numbers[2],quick_pick_numbers[3],quick_pick_numbers[4],quick_pick_numbers[5]))


main()
