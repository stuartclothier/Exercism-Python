def recite(start_verse, end_verse):
    with open('twelve-days/README.md', 'r') as file:
        data = file.read()
    
    verses = data.split('```')[1].splitlines()[1::2]

    return verses[start_verse-1:end_verse]