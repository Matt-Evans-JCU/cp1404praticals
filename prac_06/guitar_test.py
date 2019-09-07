from prac_06.guitar import Guitar

guitar = Guitar('Gibson L-5 CES', 1922,16035.40)
other = Guitar('Another Guitar',2012,1512.9)

print('{} get_age() - Expected 96. Got {}'.format(guitar.name,guitar.get_age()))
print('{} get_age() - Expected 6. Got {}'.format(other.name,other.get_age()))
print('{} is_vintage() - Expected True. Got {}'.format(guitar.name,guitar.is_vintage()))
print('{} is_vintage() - Expected False. Got {}'.format(other.name,other.is_vintage()))