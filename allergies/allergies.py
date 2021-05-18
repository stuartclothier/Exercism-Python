from math import log


class Allergies:

    all_allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                     'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score: int) -> None:
        # n determines the highest indexed allergy possible
        n = (int(log(score)/log(2)) if score else 0) \
            if score < 256 else 7

        # Create allergy list for score
        self.allergy_list = [self.all_allergies[i]
                             for i in range(n+1) if score//2**i % 2]

    def allergic_to(self, item: str) -> bool:
        return item in self.allergy_list

    @property
    def lst(self) -> list[str]:
        return self.allergy_list
