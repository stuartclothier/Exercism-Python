class Luhn:
    def __init__(self, card_num: str) -> None:
        self.num = card_num.replace(" ", "")

    def valid(self) -> bool:

        return (
            self.num.isdigit()
            and len(self.num) > 1
            and (
                (
                    sum(
                        [
                            int(digit) * 2 - 9
                            if int(digit) * 2 > 9
                            else int(digit) * 2
                            for digit in self.num[-2::-2]
                        ]
                        + [int(digit) for digit in self.num[-1::-2]]
                    )
                )
                % 10
                == 0
            )
        )
