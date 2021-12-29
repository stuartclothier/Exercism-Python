import re


class PhoneNumber:
    def __init__(self, number):
        num = re.sub("[+-.() ]+", "", number)

        if len(num) == 11:
            if num[0] == "1":
                num = num[1:]
                print(num)
            else:
                raise ValueError("11 digits must start with 1")
        if len(num) > 10:
            raise ValueError("more than 11 digits")

        if len(num) < 10:
            raise ValueError("incorrect number of digits")

        if re.search("[a-zA-Z]", num):
            raise ValueError("letters not permitted")

        if not num.isdigit():
            raise ValueError("punctuations not permitted")

        if num[0] == "0":
            raise ValueError("area code cannot start with zero")
        if num[0] == "1":
            raise ValueError("area code cannot start with one")

        if num[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if num[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = num
        self.area_code = self.number[0:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[-4:]}"
