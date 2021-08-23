import re


def abbreviate(words):
    pattern = re.compile(r"[^A-Z']")
    abbrev = "".join(
        [word[0] for word in pattern.split(words.upper()) if word]
    )

    return abbrev
