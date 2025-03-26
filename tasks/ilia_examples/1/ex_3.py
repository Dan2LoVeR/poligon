import re


def first(surname):
    surname = surname.upper()
    pattern = [
        ('ЙО', 'И'),
        ('ИО', 'И'),
        ('ЙЕ', 'И'),
        ('ИЕ', 'И'),
        ('О', 'А'),
        ('Ы', 'А'),
        ('Я', 'А'),
        ('Е', 'И'),
        ('Ё', 'И'),
        ('Э', 'И'),
        ('Ю', 'У')
    ]
    for old, new in pattern:
        surname = surname.replace(old, new)
    return surname

def second(surname):
    pattern = [
        ('Б', 'П'),
        ('З', 'С'),
        ('Д', 'Т'),
        ('В', 'Ф'),
        ('Г', 'К')
    ]
    for old, new in pattern:
        surname = surname.replace(old, new)
    return surname

def third(surname):
    pattern = [
        ('ТС', 'Ц'),
        ('ДС', 'Ц')
    ]
    for old, new in pattern:
        surname = surname.replace(old, new)
    return surname

def fourth(surname):
    seen = set()
    result = []
    for let in surname:
        if let not in seen:
            result.append(let)
    return ''.join(result)

def fivth(surname):
    let = {'Ъ', 'Ь', 'ъ', 'ь', '-'}
    filter = [char for char in surname if char not in let]
    surname = ''.join(filter)
    return surname

with open('surnames.txt', 'r', encoding='utf-8') as file:
    surnames = file.read().splitlines()

for surname in surnames:
    print(surname,'-',fivth(fourth(third(second(first(surname))))))





