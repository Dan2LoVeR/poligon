import re
import numpy as np
from scipy.spatial import distance

# Чтение файла
with open('sentences.txt', 'r') as file:
    data_list = file.readlines()

# 1. Создание массива уникальных слов в нижнем регистре
words = []
for sentence in data_list:
    # Извлекаем слова с помощью регулярного выражения (только буквы)
    sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    for word in sentence_words:
        if word not in words:
            words.append(word)

# Проверка количества уникальных слов
print(f"Количество уникальных слов: {len(words)}")  # Должно быть 254

# 2. Создание словаря {слово: индекс}
word_dict = {word: idx for idx, word in enumerate(words)}

# 3. Создание и заполнение матрицы встречаемости слов
n = len(data_list)  # Количество предложений (22)
d = len(words)  # Количество уникальных слов (254)

matrix = np.zeros((n, d), dtype=int)

for i, sentence in enumerate(data_list):
    sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    for word in sentence_words:
        j = word_dict[word]
        matrix[i, j] += 1

# 4. Вычисление косинусных расстояний между всеми парами предложений
distances = []
for i in range(n):
    for j in range(i + 1, n):  # Исключаем одинаковые пары и дубликаты (i,j) и (j,i)
        dist = distance.cosine(matrix[i], matrix[j])
        distances.append((i, j, dist))

# 5. Нахождение 5 пар с наименьшим расстоянием
top_5 = sorted(distances, key=lambda x: x[2])[:5]

# Вывод результатов
print("\nТоп 5 наиболее близких пар предложений:")
for pair in top_5:
    i, j, dist = pair
    print(f"Предложения {i} и {j}: расстояние = {dist:.4f}")
    print(f"  Предложение {i}: {data_list[i].strip()}")
    print(f"  Предложение {j}: {data_list[j].strip()}\n")

# Анализ принадлежности к классам
print("Анализ принадлежности к классам:")
for pair in top_5:
    i, j, dist = pair
    sent_i = data_list[i].lower()
    sent_j = data_list[j].lower()


    # Определение классов для каждого предложения
    def get_class(sent):
        if 'cat' in sent or 'cats' in sent:
            if 'unix' in sent or 'command' in sent or 'utility' in sent:
                return "Unix утилита cat"
            elif 'os' in sent or 'apple' in sent or 'mac' in sent or 'os x' in sent:
                return "Версии OS Apple"
            else:
                return "Упоминание кошек"
        return "Не определен"


    class_i = get_class(sent_i)
    class_j = get_class(sent_j)

    print(f"Пара {i}-{j}:")
    print(f"  Предложение {i}: {class_i}")
    print(f"  Предложение {j}: {class_j}")
    print(f"  Одинаковые классы: {class_i == class_j}\n")