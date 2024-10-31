from abc import ABC, abstractmethod


class Cipher(ABC):

    @abstractmethod
    def encryption(self, text, key):
        pass

    @abstractmethod
    def decryption(self, text, key):
        pass
    