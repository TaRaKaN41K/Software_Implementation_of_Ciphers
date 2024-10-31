from Cipher import Cipher


class TranspositionCipher(Cipher):
    def encryption(self, text, key):
        n = len(key)
        padded_text = text + ' ' * (n - len(text) % n)  # Дополнение пробелами до кратности длине ключа
        chunks = [padded_text[i:i + n] for i in range(0, len(padded_text), n)]

        # Сортируем ключ и создаем индексы для перестановки
        sorted_key = sorted(list(key))
        index_order = [key.index(char) for char in sorted_key]

        # Перестановка символов по индексам
        encrypted_text = ""
        for chunk in chunks:
            encrypted_chunk = ''.join([chunk[i] for i in index_order])
            encrypted_text += encrypted_chunk

        return encrypted_text

    def decryption(self, text, key):
        n = len(key)
        chunks = [text[i:i + n] for i in range(0, len(text), n)]

        # Сортируем ключ и создаем индексы для обратной перестановки
        sorted_key = sorted(list(key))
        index_order = [key.index(char) for char in sorted_key]

        # Создаем обратную перестановку
        inverse_index_order = [index_order.index(i) for i in range(len(index_order))]

        # Восстанавливаем исходный текст
        decrypted_text = ""
        for chunk in chunks:
            decrypted_chunk = ''.join([chunk[i] for i in inverse_index_order])
            decrypted_text += decrypted_chunk

        return decrypted_text.strip()  # Убираем пробелы, добавленные при шифровании
