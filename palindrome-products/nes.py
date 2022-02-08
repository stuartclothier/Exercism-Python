def is_palindrome(num: int) -> bool:
    """
    Given a number, return True if it is a palindrome, else return False.

    :param num: int
    :type num: int
    :return: bool
    """

    # pal = False
    # if 0 <= num < 10:
    #     pal = True

    # elif num > 9 and not pal:
    #     digs = int(log(num, 10))
    #     if num // 10 ** digs == num % 10:
    #         new_no = num // 10 % 10 ** (digs - 1)
    #         if new_no and int(log(new_no, 10)) != digs - 2:
    #             new_no = new_no // 10 ** ((digs - int(log(new_no, 10))) / 2)
    #         pal = is_palindrome(new_no)
    if num % 10 == 0:
        return False

    # store a copy of this number
    temp = num
    # calculate reverse of this number
    reverse_num = 0
    while num > 0:
        # extract last digit of this number
        digit = num % 10
        # append this digit in reveresed number
        reverse_num = reverse_num * 10 + digit
        # floor divide the number leave out the last digit from number
        num = num // 10

    return temp == reverse_num  # pal


def smallest(min_factor, max_factor):
    factors = range(min_factor, max_factor + 1)
    facs = []
    for i in range(min_factor ** 2, max_factor ** 2 + 1):
        if is_palindrome(i):
            for j in factors:
                if i % j == 0 and i // j in factors and j not in facs:
                    facs += [j, i // j]
            if facs:
                break

    return factors, i, facs


def largest(min_factor, max_factor):
    factors = range(max_factor, min_factor - 1, -1)
    facs = []
    for i in range(max_factor ** 2, min_factor ** 2 - 1, -1):
        if is_palindrome(i):
            for j in factors:
                if i % j == 0 and i // j in factors and j not in facs:
                    facs += [i // j, j]
            if facs:
                break

    return i, facs


print(largest(min_factor=10, max_factor=99))
