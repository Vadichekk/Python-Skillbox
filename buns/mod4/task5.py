def count_letters(file_name):
    # Создание словаря для подсчета частоты букв
    letter_count = {}

    # Открытие файла на чтение
    with open(file_name, 'r') as file:
        # Чтение содержимого файла
        content = file.read()

        # Обработка каждой буквы в содержимом файла
        for letter in content:
            # Проверка, является ли символ буквой
            if letter.isalpha():
                # Увеличение счетчика для данной буквы
                letter_count[letter] = letter_count.get(letter, 0) + 1

    # Сортировка словаря по значению (частоте)
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1])

    # Открытие нового файла на запись
    with open('result.txt', 'w') as result_file:
        # Запись результатов в файл
        for letter, count in sorted_letters:
            result_file.write(f'{letter}: {count}\n')

# Запрос ввода имени файла
file_name = input('Введите имя файла: ')

# Вызов функции для подсчета и записи статистики по буквам
count_letters(file_name)