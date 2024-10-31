from cipher import CaesarCipher, SubstitutionCipher, TranspositionCipher, VigenereCipher
from Enigma import Rotor, Reflector, EnigmaMachine

if __name__ == "__main__":

    plaintext = "Hello, my name is Kalashov Feodor Olegovich and I am a 4th year student of group N34481"

    # Шифр Цезаря
    caesar_cipher = CaesarCipher()
    shift = 3

    encrypted_text = caesar_cipher.encryption(text=plaintext, key=shift)
    print("Зашифрованный текст шифра Цезаря:", encrypted_text)

    decrypted_text = caesar_cipher.decryption(text=encrypted_text, key=shift)
    print("Расшифрованный текст шифра Цезаря:", decrypted_text)

    print("\n")

    # Моноалфавитный шифр замены
    substitution_cipher = SubstitutionCipher()

    substitution_encrypted = substitution_cipher.encryption(text=plaintext)
    print("Зашифрованный текст шифра замены:", substitution_encrypted)

    substitution_decrypted = substitution_cipher.decryption(text=substitution_encrypted)
    print("Расшифрованный текст шифра замены:", substitution_decrypted)

    print("\n")

    # Моноалфавитный шифр перестановки
    transposition_cipher = TranspositionCipher()

    key = "4312"

    encrypted_text = transposition_cipher.encryption(text=plaintext, key=key)
    print("Зашифрованный текст шифра перестановки:", encrypted_text)

    decrypted_text = transposition_cipher.decryption(text=encrypted_text, key=key)
    print("Расшифрованный текст шифра перестановки:", decrypted_text)

    print("\n")

    vigenere_cipher = VigenereCipher()

    key = "LEMON"

    encrypted_text = vigenere_cipher.encryption(plaintext, key)
    print("Зашифрованный текст шифра Виженера:", encrypted_text)

    decrypted_text = vigenere_cipher.decryption(encrypted_text, key)
    print("Расшифрованный текст шифра Виженера:", decrypted_text)

    print("\n")

    # Настройки машины "Энигма"
    rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch=16)  # Примерный провод ротора I
    rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch=4)  # Примерный провод ротора II
    rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch=21)  # Примерный провод ротора III
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")  # Примерный провод отражателя

    # Создание машины и шифрование
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector)
    message = "HELLOMYNAMEISKALASHOVFEODOROLEGOVICH" # "HELLOENIGMA"
    encrypted_message = enigma.encode_message(message)
    print("Зашифрованное сообщение:", encrypted_message)

    # Настройка исходной позиции для каждого ротора перед дешифрованием
    rotor1.position = 0
    rotor2.position = 0
    rotor3.position = 0

    # Дешифрование сообщения
    decrypted_message = enigma.encode_message(encrypted_message)
    print("Расшифрованное сообщение:", decrypted_message)
