"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
# TODO Figure how to print downwards so only need one return that is the problem
menu = """(H)ello
(G)oobye
(Q)uit"""
name = input('Enter name: ')
#print('(H)ello')
#print('(G)oodbye')
#print('(Q)uit')
print(menu)
choice = input('What choice do you want: ').upper()
while choice != 'Q':
    if choice == 'H':
        print('hello {}'.format(name))
    elif choice == 'G':
        print('goodbye {}'.format(name))
    else:
        print('invalid choice')
    print(menu)
    choice = input('What choice do you want: ').upper()
print("Finished.")