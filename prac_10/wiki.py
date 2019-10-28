import wikipedia

choice = input('Pick a Search Phrase or Page Title: ')
while choice != '':
    print(wikipedia.summary(choice))
    choice = input('Pick a Search Phrase or Page Title: ')