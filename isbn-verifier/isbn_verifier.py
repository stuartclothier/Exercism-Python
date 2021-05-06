# def is_valid(isbn: str):

#     raw_isbn = [int(each) for each in isbn if each.isnumeric()]

#     if len(raw_isbn) == 9 and isbn[-1] == 'X':
#         raw_isbn.append(10)

#     if len(raw_isbn) == 10:
#         return not(bool(sum(a*b for a, b in
#                             zip(range(10, 0, -1), raw_isbn)) % 11))
#     else:
#         return False

import re

def is_valid(isbn):
    isbn = isbn.replace('-','')

    isbn_pattern = re.compile('^[0-9]{9}[0-9X]$')
    if not isbn_pattern.match(isbn): return False

    total = 0
    for i in range(len(isbn)):
        value = 10 if isbn[i].upper() == 'X' else isbn[i]
        total = total + (int(value) * (10 - i))

    return True if total %11 == 0 else False