from string import ascii_uppercase, ascii_lowercase


class VigenereCipher:
    def __init__(self):
        self.upper_alphabet = ascii_uppercase
        self.lower_alphabet = ascii_lowercase


    def extend_key(self, text, key):
        """Приведение ключа к длине текста."""
        extended_key = []
        key_index = 0
        for char in text:
            if char.isalpha():  # Проверяем, является ли символ буквой
                extended_key.append(key[key_index % len(key)])  # Добавляем букву из ключа
                key_index += 1  # Увеличиваем индекс ключа только для букв
            else:
                extended_key.append(char)  # Оставляем небуквенные символы без изменений
        return ''.join(extended_key)

    def encryption(self, text, key):
        """Шифрование текста с использованием шифра Виженера."""
        result = []
        extended_key = self.extend_key(text, key)  # Расширяем ключ до длины текста
        for i, char in enumerate(text):
            if char.isupper():
                shift_base = ord('A')
                shift = ord(extended_key[i].upper()) - ord('A')  # Сдвиг для заглавных
                result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            elif char.islower():
                shift_base = ord('a')
                shift = ord(extended_key[i].lower()) - ord('a')  # Сдвиг для строчных
                result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            else:
                result.append(char)  # Оставляем пробелы и символы без изменений
        return ''.join(result)

    def decryption(self, text, key):
        """Дешифрование текста с использованием шифра Виженера."""
        result = []
        extended_key = self.extend_key(text, key)  # Расширяем ключ до длины текста
        for i, char in enumerate(text):
            if char.isupper():
                shift_base = ord('A')
                shift = ord(extended_key[i].upper()) - ord('A')  # Сдвиг для заглавных
                result.append(chr((ord(char) - shift_base - shift + 26) % 26 + shift_base))
            elif char.islower():
                shift_base = ord('a')
                shift = ord(extended_key[i].lower()) - ord('a')  # Сдвиг для строчных
                result.append(chr((ord(char) - shift_base - shift + 26) % 26 + shift_base))
            else:
                result.append(char)  # Оставляем пробелы и символы без изменений
        return ''.join(result)