def convert(number):
    drops = ['','','']

    if no % 3 == 0:
        drops[0] = "pling"
    if no % 5 == 0:
        drops[1] = "plang" 
    if no % 7 == 0:
        drops[2] = "plong" 

    if drops == ['','','']:
        number
    else:
        ''.join(drops)
