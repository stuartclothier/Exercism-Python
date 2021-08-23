# Letter values.
my_dict = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
}

def score(
    word: str, dl: str = "", tl: str = "", dw: bool = False, tw: bool = False
) -> int:

    # Check word is only alpha characters.
    if not word.isalpha() and word:
        raise ValueError("Error: Non-alpha characters in string.")

    # Add extra letters to word for double/triple letter score.
    if dl:
        if dl not in word:
            raise ValueError("Error: Double letter not in word.")
        word = word + dl

    if tl:
        if dl not in word:
            raise ValueError("Error: Triple letter not in word.")
        word = word + 2 * tl

    # Calculate score.
    score = sum(
        [
            v
            for k, v in my_dict.items()
            for letter in word.upper()
            if letter in k
        ]
    )

    # Multiply score if double or triple word.
    if dw:
        score = 2 * score

    if tw:
        score = 3 * score

    return score

print(score("hello", dl='h',tl='h', tw=True))