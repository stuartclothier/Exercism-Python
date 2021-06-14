import re

# using findall
def count_words(sentence):

    pattern = re.compile(r"[a-z0-9']+")

    word_list = [word.strip("'") for word in pattern.findall(sentence.lower())]
    return {i: word_list.count(i) for i in word_list}


# using split
def count_words(sentence):

    pattern = re.compile(r"[^a-z0-9']|_")
    word_list = [word.strip("'")
                 for word in pattern.split(sentence.lower()) if word]
    return {i: word_list.count(i) for i in word_list}
