def is_paired(input_string):
    """
    Given a string, return True if all brackets are paired
    in the correct order, otherwise return False

    :param input_string: The string to be tested
    :return: True or False
    """

    brackets = {")": "(", "}": "{", "]": "["}

    bracket_list = [each for each in input_string if each in "(){}[]"]

    state = []

    for each in bracket_list:
        if each in brackets:
            if state and brackets[each] == state[-1]:
                state = state[:-1]
                continue
            else:
                return False
        state.append(each)

    return not state
