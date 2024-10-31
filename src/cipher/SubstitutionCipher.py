from random import shuffle
from string import ascii_uppercase, ascii_lowercase

from Cipher import Cipher


class SubstitutionCipher(Cipher):
    def __init__(self, key=None):
        if key is None:
            upper_key = list(ascii_uppercase)
            lower_key = list(ascii_lowercase)
            shuffle(upper_key)
            shuffle(lower_key)
            self.upper_key = ''.join(upper_key)
            self.lower_key = ''.join(lower_key)
        else:
            self.upper_key, self.lower_key = key

        self.upper_alphabet = ascii_uppercase
        self.lower_alphabet = ascii_lowercase

    def encryption(self, text):
        substitution_dict = str.maketrans(
            self.upper_alphabet + self.lower_alphabet,
            self.upper_key + self.lower_key
        )
        return text.translate(substitution_dict)

    def decryption(self, text):
        substitution_dict = str.maketrans(
            self.upper_key + self.lower_key,
            self.upper_alphabet + self.lower_alphabet
        )
        return text.translate(substitution_dict)
