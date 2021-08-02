import re


def count_words(sentence):

    # Create list of words
    pattern = re.compile(r"[^a-z0-9']|_")
    word_list = [
        word.strip("'") for word in pattern.split(sentence.lower()) if word
    ]

    # Count each word
    count = dict()
    for i in word_list:
        count[i] = count.get(i, 0) + 1

    return count
