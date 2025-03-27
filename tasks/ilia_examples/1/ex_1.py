# Импорт модуля для работы с регулярными выражениями
import re

# Открытие файла 'input.txt' в режиме чтения с кодировкой UTF-8
with open('input.txt', 'r', encoding='utf-8') as file:
    # Чтение всего содержимого файла в переменную text
    text = file.read()

# Удаление HTML/XML-тегов (всего, что находится между < и >) и замена их на пробел
cleaned_text = re.sub(r'<[^>]+>', ' ', text)
# Удаление всех цифр из текста
cleaned_text = re.sub(r'\d+', '', cleaned_text)
# Удаление всех знаков пунктуации (всех символов, кроме букв, цифр и пробелов)
cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)

# Приведение всего текста к нижнему регистру
cleaned_text = cleaned_text.lower()
# Разбиение текста на список слов (разделитель - пробел)
words_list = cleaned_text.split()
# Сортировка списка слов в алфавитном порядке
words_list = sorted(words_list)

# Создание словаря, где ключи - уникальные слова из списка,
# а значения - количество их вхождений в исходном тексте
D = dict(zip(words_list, [words_list.count(i) for i in words_list]))  # Делаем словарь из списка
# Вывод получившегося словаря
print(D)