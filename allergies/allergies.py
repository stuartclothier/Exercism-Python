from math import log


class Allergies:
    alles_list = ['eggs',
                  'peanuts',
                  'shellfish',
                  'strawberries',
                  'tomatoes',
                  'chocolate',
                  'pollen',
                  'cats']

    def __init__(self, score: int) -> None:

        base2 = []

        # convert score to base 2 list if score isn't 0.
        if score:
            n = int(log(score)/log(2))

            for i in range(n, -1, -1):
                if score//2**i:
                    base2.append(score//2**i)
                    score = score-2**i
                else:
                    base2.append(0)

        # Create list of allergies
        self.allergy_list = [b for a, b in zip(
            base2[-1::-1], self.alles_list) if a]
        return None

    def allergic_to(self, item: str) -> bool:
        return item in self.allergy_list

    @property
    def lst(self) -> list[str]:
        return self.allergy_list
