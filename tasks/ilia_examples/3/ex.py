import re
from collections import defaultdict
import math
from itertools import combinations


# Загрузка данных
with open('tz1_data.txt', 'r', encoding='utf-8') as f:
    sentences = [line.strip() for line in f if line.strip()]


# 1. Предобработка данных (без лемматизации)
def preprocess_text(text):
    # Удаление знаков препинания и приведение к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text


processed_sentences = [preprocess_text(sentence) for sentence in sentences]


# 2. Построение TF-IDF модели
def build_tfidf_matrix(documents):
    # Создание словаря терминов
    vocab = set()
    word_doc_count = defaultdict(int)

    # Подсчет документов, содержащих каждое слово
    doc_words = []
    for doc in documents:
        words = doc.split()
        doc_words.append(words)
        for word in set(words):
            vocab.add(word)
            word_doc_count[word] += 1

    vocab = sorted(vocab)
    word_to_idx = {word: idx for idx, word in enumerate(vocab)}
    n_docs = len(documents)

    # Построение матрицы TF-IDF
    tfidf_matrix = []
    for words in doc_words:
        # Подсчет TF
        tf = defaultdict(float)
        word_count = len(words)
        for word in words:
            tf[word] += 1 / word_count

        # Вычисление TF-IDF для каждого слова
        vector = [0.0] * len(vocab)
        for word, tf_val in tf.items():
            idf = math.log(n_docs / (1 + word_doc_count[word]))
            vector[word_to_idx[word]] = tf_val * idf

        tfidf_matrix.append(vector)

    return tfidf_matrix, vocab


tfidf_matrix, vocab = build_tfidf_matrix(processed_sentences)


# 3. Вычисление косинусного расстояния
def cosine_distance(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    norm1 = math.sqrt(sum(v * v for v in vec1))
    norm2 =math.sqrt(sum(v * v for v in vec2))
    return 1 - (dot_product / (norm1 * norm2)) if norm1 and norm2 else 1.0


# Создание списка пар с расстояниями
pairs = []
n = len(sentences)
for i, j in combinations(range(n), 2):
    distance = cosine_distance(tfidf_matrix[i], tfidf_matrix[j])
    pairs.append((i, j, distance))

# Сортировка пар по расстоянию
pairs.sort(key=lambda x: x[2])


# 4. Кластеризация документов
def cluster_documents(pairs, n_clusters=3, top_pairs=25):
    # Выбираем топ-N пар с минимальным расстоянием
    selected_pairs = pairs[:top_pairs]

    # Создаем граф связей
    graph = defaultdict(set)
    for i, j, _ in selected_pairs:
        graph[i].add(j)
        graph[j].add(i)

    # Кластеризация с помощью объединения
    clusters = []
    visited = set()

    for node in range(n):
        if node not in visited:
            # Начинаем новый кластер
            cluster = set()
            stack = [node]

            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    cluster.add(current)
                    # Добавляем соседей
                    stack.extend(graph[current] - visited)

            clusters.append(cluster)

    # Если кластеров больше чем нужно, объединяем самые маленькие
    while len(clusters) > n_clusters:
        # Находим два ближайших кластера
        min_dist = float('inf')
        merge_pair = (0, 1)

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                # Вычисляем среднее расстояние между кластерами
                total = 0
                count = 0
                for a in clusters[i]:
                    for b in clusters[j]:
                        for pair in pairs:
                            if (a == pair[0] and b == pair[1]) or (a == pair[1] and b == pair[0]):
                                total += pair[2]
                                count += 1
                                break
                if count > 0:
                    avg_dist = total / count
                    if avg_dist < min_dist:
                        min_dist = avg_dist
                        merge_pair = (i, j)

        # Объединяем кластеры
        if min_dist != float('inf'):
            i, j = merge_pair
            clusters[i].update(clusters[j])
            del clusters[j]
        else:
            break

    return clusters


clusters = cluster_documents(pairs)

# Вывод результатов кластеризации
print("Результаты кластеризации:")
for i, cluster in enumerate(clusters):
    print(f"\nКластер {i + 1}:")
    for idx in sorted(cluster):
        print(f"{idx + 1}: {sentences[idx]}")