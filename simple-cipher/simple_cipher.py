class Cipher:
    def __init__(self, key=None):
        self.key = [ord(each) - 97 for each in key]

    def encode(self, text):
        text_list = Cipher(text).key
        if len(self.key)<len(text_list):
            self.key = self.key*(len(text_list)//len(self.key)+1)
        coded = [chr((x + y) % 26 + 97) for x, y in zip(text_list, self.key)]

        return "".join(coded)

    def decode(self, text):
        text_list = Cipher(text).key
        if len(self.key)<len(text_list):
            self.key = self.key*(len(text_list)//len(self.key)+1)
        
        coded = [chr((x - y) % 26 + 97) for x, y in zip(text_list, self.key)]

        return "".join(coded)

# cipher = Cipher("abcdefghij")
# plaintext = "aaaaaaaaaa"


# print(cipher.encode(plaintext))
# print(cipher.decode(cipher.encode(plaintext)))

# cipher = Cipher("abc")
# plaintext = "iamapandabear"
# print(cipher.encode(plaintext))