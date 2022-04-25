def get_lines(bottles):
    factors = {-1: "99 bottles", 0: "No more bottles", 1: "1 bottle"}

    if bottles in factors:
        factor = factors[bottles]
    else:
        factor = f"{bottles} bottles"
    return factor


def first_line(bottles):
    factor = get_lines(bottles)
    return f"{factor} of beer on the wall, {str.lower(factor)} of beer."


def second_line(bottles):
    if bottles == -1:
        start = "Go to the store and buy some more"
    elif bottles == 0:
        start = "Take it down and pass it around"
    else:
        start = "Take one down and pass it around"
    factor = get_lines(bottles)
    return f"{start}, {str.lower(factor)} of beer on the wall."


def recite(start, take=1):

    bottles = range(start, start - take, -1)

    verse = [
        unpacked
        for b in bottles
        for unpacked in ["", first_line(b), second_line(b - 1)]
    ]

    return verse[1:]
