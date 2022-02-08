"""
Given a range of numbers, these functions find the largest or smallest
palindromes which are products of two numbers within that range
"""


def is_palindrome(num: int) -> bool:
    """
    Given a number, return True if it is a palindrome, else return False.

    :param num: int
    :return: bool
    """

    if num % 10 == 0:
        return False

    temp = num
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10

    return temp == reverse_num


def val(min_factor: int, max_factor: int) -> None:
    """
    Validate min is less than max

    :param min_factor: int - the smallest number to be multiplied
    :param max_factor: int - The largest number to consider for
    the product of two numbers
    :return: Nothing
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    return None


def pal(start: int, stop: int, order: int) -> list[int, list[int]]:
    """
    Find the smallest or largest palindrome made from the product of
    two numbers

    :param start: The first number to check for palindromes
    :param stop: The last number to check for palindromes
    :param order: 1 for ascending/smallest, -1 for descending/largest
    :return: The palindrome and the factors.
    """

    factors = range(start, stop + order, order)
    facs = []
    for i in range(start ** 2, stop ** 2 + order, order):
        if is_palindrome(i):
            for j in factors:
                if i % j == 0 and i // j in factors:
                    facs += [[j, i // j][::order]]
            if facs:
                break
        if not facs:
            i = None

    return i, facs


def smallest(min_factor: int, max_factor: int) -> list[int, list[int]]:
    """
    Find the smallest palindrome number between two numbers

    :param min_factor: int - The smallest number to consider when
    looking for a palindrome
    :param max_factor: int - The largest possible factor
    :return: list - The smallest palindrome and the factors that make it up.
    """
    val(min_factor, max_factor)
    return pal(min_factor, max_factor, 1)


def largest(min_factor: int, max_factor: int) -> list[int, list[int]]:
    """
    Find the largest palindrome made from the product of two numbers
    between min_factor and max_factor

    :param min_factor: int - The smallest number to consider when
    looking for a palindrome
    :param max_factor: int - The largest possible factor
    :return: list - The largest palindrome and the factors that make it up.
    """
    val(min_factor, max_factor)
    return pal(max_factor, min_factor, -1)
