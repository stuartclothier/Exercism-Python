import math


def factors(value):
    i = 2
    res_set = []
    while value != 1:
        if not value % i:
            res_set.append(i)
            value //= i
        else:
            i += 1

    return res_set
