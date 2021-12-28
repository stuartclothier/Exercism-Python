aminos = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
}

stop = ["UAA", "UAG", "UGA"]


def proteins(strand):
    pros = []
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        if codon in stop:
            break
        for amino in aminos.items():
            if codon in amino[1]:
                pros.append(amino[0])

    return pros
