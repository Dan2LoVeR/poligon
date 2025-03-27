import re
import numpy as np
from scipy.spatial import distance


def cat_class(sent):
    if 'cat' in sent or 'cats' in sent:
        if 'unix' in sent or 'command' in sent or 'utility' in sent:
            return "Unix утилита cat"
        elif 'os' in sent or 'apple' in sent or 'mac' in sent or 'os x' in sent:
            return "Версии OS Apple"
        else:
            return "Упоминание кошек"
    return "Не определен"

def get_distance(item):
    return item[2]

with open('sentences.txt', 'r') as file:
    data_list = file.readlines()

words = []
for sentence in data_list:
    sentence_words = re.findall(r"\b[a-zA-Z]+\b", sentence.lower())
    for word in sentence_words:
        if word not in words:
            words.append(word)

word_dict = {word: idx for idx, word in enumerate(words)}

n = len(data_list)
d = len(words)

matrix = np.zeros((n, d), dtype=int)

for i, sentence in enumerate(data_list):
    sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    for word in sentence_words:
        j = word_dict[word]
        matrix[i, j] += 1
        print(matrix)

distances = []
for i in range(n):
    for j in range(i + 1, n):
        dist = distance.cosine(matrix[i], matrix[j])
        distances.append((i, j, dist))


top_5 = sorted(distances, key=get_distance)[:5]

print("5 наиболее близких пар предложений:")
for pair in top_5:
    i, j, dist = pair

    sent_i = data_list[i].lower()
    sent_j = data_list[j].lower()

    class_i = cat_class(sent_i)
    class_j = cat_class(sent_j)

    print(f"Предложения {i} и {j}: расстояние = {dist:.4f} | Одинаковые классы: {class_i == class_j}")

