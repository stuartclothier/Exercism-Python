def square(number):
    if not 1 <= number <= 64:
        raise ValueError("Number must be between 1 and 64.")

    # Mathematical solution
    # return 2 ** (number - 1)

    # Bitwise solution
    return 1 << (number - 1)


def total():
    return 2 * square(64) - 1
