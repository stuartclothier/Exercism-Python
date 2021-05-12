def is_isogram(string: str):
    string = ''.join(filter(str.isalpha, string.lower()))

    return next((False for x, y in enumerate(string[:-1]) if
                 string.find(y, x+1) != -1), True)
