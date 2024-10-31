from Cipher import Cipher


class CaesarCipher(Cipher):
    def encryption(self, text, key):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift_base + key) % 26 + shift_base)
            else:
                result += char
        return result

    def decryption(self, text, key):
        return self.encryption(text, -key)
