"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car
import random

class UnreliableCar(Car):

    def __init__(self,name,fuel,reliability):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_number = random.randint(0,101)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven