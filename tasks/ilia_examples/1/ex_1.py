import re

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

cleaned_text = re.sub(r'<[^>]+>', ' ', text)
cleaned_text = re.sub(r'\d+', '', cleaned_text)
cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)

cleaned_text = cleaned_text.lower()
words_list = cleaned_text.split()
words_list = sorted(words_list)

# Замените в следующей строке букву s на имя переменной, в которой хранится ваш список
D = dict(zip(words_list, [words_list.count(i) for i in words_list]))  # Делаем словарь из списка
print(D)
