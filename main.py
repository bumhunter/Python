def main():
    print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
    print("Нажмите Enter и начнем")
    input()  # вводим enter
    dictionary = {}  # создаем пустой словарь для готовых слов
    results = []
    code = createDict()  # получаем побуквенный словарь из базы
    while True:  # вызываем меню
        print(' 1 - Добавить слово (регистр не учитывается) \n 2 - Расшифровать слово \n 3 - Посмотреть словарь \n 0 - Выход ')
        choice = str(input())  # выбор пункта меню
        if choice == '0':
            size = len(results)
            success = results.count(True)
            failure = results.count(False)
            print("Количество попыток: " + str(size))
            print("Удачных попыток: " + str(success))
            print("Неудачных попыток: " + str(failure))
            break  # при вводе 0 из меню выходим из программы
        if choice == '1':
            dict_update = {**dictionary, **text_morse(code)}  # при добавлении нового слова получаем морзе-код введенного слова
            dictionary = dict_update   # обновляем словарь готовых слов, добавляем новое слово и его код
        if choice == '2':
            result = guess_word(dictionary)
            results.append(result)
        if choice == '3':
            print(code)  # при выборе пункта меню 3 выводим побуквенный словарь на экран


def guess_word(dictionary):
    import random
    random_word = random.choice(list(dictionary))
    print("Угадайте слово: " + dictionary[random_word])
    answer = input()
    answer = answer.upper()
    if answer == random_word:
        print("Верно! " + random_word)
        return True
    else:
        print("Неправильно! Правильное слово " + get_key(dictionary, dictionary[random_word]))
        return False


def get_key(dictionary, value):
    for k, v in dictionary.items():
        if v == value:
            return k

def text_morse(code):
    morse_word = ''
    new_word = {}
    word = str(input('Введите слово: '))
    word = word.upper()
    for letter in word:
        morse_word += code[letter] + " "
    new_word[word] = morse_word
    print("Вы добавили новое слово в словарь. " + morse_word)
    return new_word


def createDict():
    code = {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----'}
    return code
# требуется хотя бы две пустых строки между функциями


if __name__ == '__main__':
    main()
