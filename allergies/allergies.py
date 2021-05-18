from math import log


class Allergies:

    all_allergies = ['eggs',
                     'peanuts',
                     'shellfish',
                     'strawberries',
                     'tomatoes',
                     'chocolate',
                     'pollen',
                     'cats']

    def __init__(self, score: int) -> None:
        self.allergy_list = [self.all_allergies[i]
                             for i in range(8) if score//2**i % 2]

    def allergic_to(self, item: str) -> bool:
        return item in self.allergy_list

    @property
    def lst(self) -> list[str]:
        return self.allergy_list
