import re


def abbreviate(words):
    pattern = re.compile(r"[^A-Z']")
    abbrev = "".join(
        [word[0] for word in pattern.split(words.upper()) if word]
    )

    return abbrev


def abbreviate(words):
    return "".join(
        word[0] for word in words.replace("-", " ").replace("_", " ").split()
    ).upper()


def abbreviate(words):
    return "".join(
        filter(lambda s: s.isupper(), words.replace("'", "").title())
    )
