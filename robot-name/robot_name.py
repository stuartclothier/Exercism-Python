import string
import random

robot_list = set()

class Robot:

    def __init__(self):
        self.reset()

    def reset(self):

        self.name = ''.join(random.choices(
                    string.ascii_uppercase, k=2)+
                    random.choices(string.digits, k=3))

        if self.name in robot_list:
            self.reset()

        robot_list.add(self.name)