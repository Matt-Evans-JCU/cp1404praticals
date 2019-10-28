import wikipedia

choice = input('Pick a Search Phrase or Page Title: ')
while choice != '':
    try:
        wiki_page = wikipedia.page(choice)
        print(wiki_page.title)
        print(wiki_page.summary)
        print(wiki_page.url)
        choice = input('Pick a Search Phrase or Page Title: ')
    except wikipedia.exceptions.DisambiguationError as e:
        print("These are your options")
        print(e.options)
        choice = input('Pick a Search Phrase or Page Title: ')