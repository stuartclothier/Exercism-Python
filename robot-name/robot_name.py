import string
import random


class Robot:

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = f"{''.join(random.choices(string.ascii_uppercase,k = 2))}{''.join(random.choices(string.digits,k=3))}"


print(Robot().name)
print(Robot().name)
