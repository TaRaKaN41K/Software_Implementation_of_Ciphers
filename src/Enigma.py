class Rotor:
    def __init__(self, wiring, notch, position=0):
        self.wiring = wiring  # Проводка ротора — задает, как каждая буква изменяется
        self.notch = notch  # Позиция, при которой ротор передает вращение дальше
        self.position = position  # Текущая позиция ротора

    def encode_forward(self, char):
        """Кодирование символа при движении вперед через ротор."""
        index = (ord(char) - 65 + self.position) % 26  # Сдвиг символа с учетом позиции ротора
        encoded_char = self.wiring[index]  # Получение зашифрованного символа
        return chr((ord(encoded_char) - 65 - self.position) % 26 + 65)  # Преобразование назад

    def encode_backward(self, char):
        """Кодирование символа при обратном движении через ротор."""
        # Поиск, какой символ соответствует текущему, при обратном движении
        index = (self.wiring.index(chr((ord(char) - 65 + self.position) % 26 + 65)) - self.position) % 26
        return chr(index + 65)  # Вернуть символ

    def rotate(self):
        """Поворачивает ротор, возвращает True, если достигнута позиция щелчка."""
        self.position = (self.position + 1) % 26  # Изменение позиции ротора
        return self.position == self.notch  # Проверка, достигнут ли щелчок


class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring  # Проводка отражателя

    def reflect(self, char):
        """Отражает символ, перенаправляя его обратно через роторы."""
        return self.wiring[ord(char) - 65]  # Возвращает символ по проводке


class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encode_character(self, char):
        """Шифрует символ, пропуская его через роторы, отражатель и снова через роторы."""
        # Прямое прохождение через роторы
        for rotor in self.rotors:
            char = rotor.encode_forward(char)

        # Отражение
        char = self.reflector.reflect(char)

        # Обратное прохождение через роторы
        for rotor in reversed(self.rotors):
            char = rotor.encode_backward(char)

        return char

    def step_rotors(self):
        """Поворачивает роторы, учитывая положение щелчков."""
        # Начинаем с первого ротора
        rotate_next = self.rotors[0].rotate()  # Вращаем первый ротор
        if rotate_next:  # Если он достиг щелчка, вращаем второй
            rotate_next = self.rotors[1].rotate()
            if rotate_next:  # Если второй достиг щелчка, вращаем третий
                self.rotors[2].rotate()

    def encode_message(self, message):
        """Шифрует целое сообщение."""
        encrypted_message = ""
        for char in message:
            self.step_rotors()  # Вращаем роторы перед шифрованием символа
            encrypted_message += self.encode_character(char)
        return encrypted_message
