def is_palindrome(word):
    # Удаляем все пробелы из слова и переводим его в нижний регистр
    word = word.replace(" ", "").lower()

    # Проверяем, можно ли из букв в слове составить палиндром
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # Если количество букв с нечетным количеством больше 1, то из слова невозможно составить палиндром
    if odd_count > 1:
        return False
    else:
        return True


def build_palindrome(word):
    palindrome = ""
    char_count = {}

    # Удаляем все пробелы из слова и переводим его в нижний регистр
    word = word.replace(" ", "").lower()

    # Выводим сообщение, если из слова невозможно составить палиндром
    if not is_palindrome(word):
        print("Из данного слова невозможно составить палиндром.")
        return

    # Собираем палиндром в центре, добавляя буквы с нечетным количеством
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        if char_count[char] % 2 != 0:
            palindrome += char

    # Собираем остальную часть палиндрома, добавляя буквы с четным количеством
    for char in word:
        if char_count[char] % 2 == 0:
            palindrome = char + palindrome + char

    # Выводим полученный палиндром
    print("Палиндром:", palindrome)


# Ввод слова от пользователя
word = input("Введите слово: ")

# Проверка возможности составить палиндром и вывод полученного палиндрома
build_palindrome(word)