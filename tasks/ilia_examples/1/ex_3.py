# Импорт модуля для работы с регулярными выражениями (хотя в данном коде не используется)
import re

# Функция для замены гласных букв по определенным правилам
def first(surname):
    # Приводим фамилию к верхнему регистру
    surname = surname.upper()
    # Паттерны для замены: (что заменить, на что заменить)
    pattern = [
        ('ЙО', 'И'),  # ЙО → И
        ('ИО', 'И'),   # ИО → И
        ('ЙЕ', 'И'),   # ЙЕ → И
        ('ИЕ', 'И'),   # ИЕ → И
        ('О', 'А'),     # О → А
        ('Ы', 'А'),     # Ы → А
        ('Я', 'А'),     # Я → А
        ('Е', 'И'),     # Е → И
        ('Ё', 'И'),     # Ё → И
        ('Э', 'И'),     # Э → И
        ('Ю', 'У')      # Ю → У
    ]
    # Применяем все замены из паттерна
    for old, new in pattern:
        surname = surname.replace(old, new)
    return surname

# Функция для замены согласных букв по определенным правилам
def second(surname):
    # Паттерны для замены согласных
    pattern = [
        ('Б', 'П'),  # Б → П
        ('З', 'С'),   # З → С
        ('Д', 'Т'),   # Д → Т
        ('В', 'Ф'),   # В → Ф
        ('Г', 'К')    # Г → К
    ]
    # Применяем все замены
    for old, new in pattern:
        surname = surname.replace(old, new)
    return surname

# Функция для замены сочетаний согласных
def third(surname):
    # Паттерны для замены сочетаний букв
    pattern = [
        ('ТС', 'Ц'),  # ТС → Ц
        ('ДС', 'Ц')   # ДС → Ц
    ]
    # Применяем замены
    for old, new in pattern:
        surname = surname.replace(old, new)
    return surname

# Функция для удаления повторяющихся символов
def fourth(surname):
    # Множество для отслеживания уже встреченных символов
    seen = set()
    # Список для хранения уникальных символов
    result = []
    # Перебираем все символы в фамилии
    for let in surname:
        # Если символ еще не встречался, добавляем его в результат
        if let not in seen:
            result.append(let)
            seen.add(let)
    # Собираем результат в строку
    return ''.join(result)

# Функция для удаления мягких/твердых знаков и дефисов
def fivth(surname):
    # Символы, которые нужно удалить
    let = {'Ъ', 'Ь', 'ъ', 'ь', '-'}
    # Фильтруем фамилию, оставляя только символы не из списка let
    filter = [char for char in surname if char not in let]
    # Собираем отфильтрованные символы обратно в строку
    surname = ''.join(filter)
    return surname

# Открываем файл с фамилиями для чтения (кодировка UTF-8)
with open('surnames.txt', 'r', encoding='utf-8') as file:
    # Читаем все строки файла, удаляя символы переноса строки
    surnames = file.read().splitlines()

# Обрабатываем каждую фамилию из списка
for surname in surnames:
    # Применяем все функции последовательно и выводим результат
    # Порядок обработки: first → second → third → fourth → fivth
    print(surname, '-', fivth(fourth(third(second(first(surname))))))