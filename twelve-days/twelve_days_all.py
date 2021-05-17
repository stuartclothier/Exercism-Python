def recite(start_verse, end_verse):
    nth = ['first','second','third','fourth','fifth','sixth',
    'seventh','eighth','ninth','tenth','eleventh','twelfth']
    
    verses = ["twelve Drummers Drumming, ", "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ", "nine Ladies Dancing, " , 
    "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ", "five Gold Rings, ", 
    "four Calling Birds, ", "three French Hens, ", 
    "two Turtle Doves, and ", "a Partridge in a Pear Tree."]

    return [f"On the {nth[verse-1]} day of Christmas my true love"
    " gave to me: "+''.join(verses[-verse:]) for verse in 
    range(start_verse,end_verse+1)]

# def recite(start_verse, end_verse):
#     with open('twelve-days/README.md', 'r') as file:
#         data = file.read()
    
#     verses = data.split('```')[1].splitlines()[1::2]

#     return verses[start_verse-1:end_verse]