EXPECTED_BAKE_TIME = 40


def preparation_time_in_minutes(layers):
    """Calculate the preperation time in minute.

    :param layers: int the number of layers in the lasagne.

    Function that takes the number of layers in the lasagne and calculates the
    total preperation time in minutes. Each layer takes two minutes to prepare.
    """
    return layers * 2


PREPARATION_TIME = preparation_time_in_minutes(2)


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """

    return preparation_time_in_minutes(layers) + elapsed_bake_time
