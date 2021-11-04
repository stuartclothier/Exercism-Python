from random import randint


class Cipher:
    def __init__(self, key=None):
        if key:
            if not key.isalpha():
                raise ("Key must be alpha characters only")
            self.key = str.lower(key)
        else:
            self.key = "".join(chr(randint(97, 122)) for i in range(100))

    def encode(self, text):
        # ensure key is long enough to cover text
        if len(self.key) < len(text):
            self.key = self.key * (len(text) // len(self.key) + 1)

        coded = [
            chr((ord(x) + ord(y) - 194) % 26 + 97)
            for x, y in zip(text, self.key)
        ]

        return "".join(coded)

    def decode(self, text):
        # ensure key is long enough to cover text
        if len(self.key) < len(text):
            self.key = self.key * (len(text) // len(self.key) + 1)

        coded = [
            chr((ord(x) - ord(y) + 26) % 26 + 97)
            for x, y in zip(text, self.key)
        ]

        return "".join(coded)
