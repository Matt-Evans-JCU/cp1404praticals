for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 110, 10):
    print(i, end=' ')
print()
#TODO This can be done better
#for i in range(0, 20):
#    print(-1*i+20, end=' ')
#print()
for i in range(20,0,-1):
    print(i, end=' ')
print()
stars = int(input("What Integer Number you Pick: "))
for i in range(stars):
    print('*', end='')
print()
stars = int(input("What Integer Number you Pick: "))
for i in range(stars+1):
    print('*' *i)
