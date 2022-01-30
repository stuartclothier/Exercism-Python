"""
Given a range of numbers, these functions find the largest or smallest
palindromes which are products of two numbers within that range
"""
from math import log


def prod_list(max_factor: int, min_factor: int) -> dict[int : list[int]]:
    """
    Create a dictionary with the product of two numbers as the key and the
    list of the two numbers as the value.

    :param max_factor: int - the maximum value of both factors
    :param min_factor: int - The lowest number you want to check
    :return: dict() A dictionary with the key being the product of the factors
    and the value being a list of the factors.
    """

    res = dict()
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            if i * j in res:
                res[i * j].append([i, j])
            else:
                res[i * j] = [[i, j]]
    return res


def is_palindrome(num: int) -> bool:
    """
    Given a number, return True if it is a palindrome, else return False.

    :param num: int
    :type num: int
    :return: bool
    """

    pal = False
    if 0 <= num < 10:
        pal = True

    elif num > 9 and not pal:
        digs = int(log(num, 10))
        if num // 10 ** digs == num % 10:
            new_no = num // 10 % 10 ** (digs - 1)
            pal = is_palindrome(new_no)

    return pal


def palindrome(
    max_factor: int, min_factor: int, reverse: bool = False
) -> tuple[int, list[int]]:
    """
    Given a range of numbers, find the smallest or largest
    (dependant on reverse param) palindrome which is a product
    of two numbers within that range.

    :param max_factor: int - the maximum factor
    :param min_factor: int - the smallest factor to consider default 0
    :param reverse: bool - If True, returns highest palindrome, defaults False
    :return: tuple - (palindrome, list[factors]).
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    res = prod_list(max_factor, min_factor)

    for each in sorted(list(res), reverse=reverse):
        if is_palindrome(each):
            pal = each
            break

    return pal, res[pal]


def largest(max_factor: int, min_factor: int = 0) -> tuple[int, list[int]]:
    """Given a range of numbers, find the largest palindrome which
    is the product of two numbers within that range.

    :param min_factor: int - with a default value of 0
    :param max_factor: int
    :return: tuple - (palindrome, list[factors]).
    """

    return palindrome(max_factor, min_factor, True)


def smallest(max_factor: int, min_factor: int = 0) -> tuple[int, list[int]]:
    """Given a range of numbers, find the smallest palindrome which
    is the products of two numbers within that range.

    :param min_factor: int - with a default value of 0
    :param max_factor: int
    :return: tuple - (palindrome, list[factors])
    """

    return palindrome(max_factor, min_factor)


print(smallest(min_factor=100, max_factor=999))
print(is_palindrome(10201))
