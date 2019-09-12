# THIRTY_DAYS = [4, 6, 9, 11]
# THIRTY_ONE_DAYS = [1, 3, 4, 7, 8, 10, 12]
# FEBRUARY = 29
# LEAP_YEAR = 28
MONTH_DAYS = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31, 'Leap Year': 28}


class Data:

    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return '{}/{}/{}'.format(self.day, self.month, self.year)

    def add_days(self, n):
        self.day += n
        if self.month == 2 & self.year % 4 == 0:
            if self.day > MONTH_DAYS['Leap Year']:
                self.month += 1
                self.day = 1
        elif self.day > MONTH_DAYS[self.month]:
            self.month += 1
            self.day = 1
        if self.month == 13:
            self.year += 1
            self.month = 1


matt = Data(year=4)
matt.add_days(60)
print(matt)
