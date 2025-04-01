# Импорт необходимых библиотек
import re  # Для работы с регулярными выражениями
from collections import defaultdict  # Для словарей с значениями по умолчанию
import math  # Для математических операций
from itertools import combinations  # Для создания комбинаций элементов

# Загрузка данных из файла
with open('tz1_data.txt', 'r', encoding='utf-8') as file:
    # Читаем строки, удаляем пробелы и оставляем непустые строки
    sentences = [line.strip() for line in file if line.strip()]


# Функция предварительной обработки текста
def preprocess_text(text):
    """
    Очищает текст от пунктуации и приводит к нижнему регистру
    Args:
        text: исходная строка текста
    Returns:
        обработанная строка текста
    """
    # Удаляем все символы, кроме букв, цифр и пробелов
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text


# Применяем предобработку ко всем предложениям
processed_sentences = [preprocess_text(sentence) for sentence in sentences]


# Функция построения TF-IDF матрицы
def build_tfidf_matrix(documents):
    """
    Создает TF-IDF матрицу для набора документов
    Args:
        documents: список обработанных текстов
    Returns:
        tfidf_matrix: матрица TF-IDF
        vocabulary: список уникальных слов
    """
    # Инициализация структур данных
    vocabulary = set()  # Множество для хранения уникальных слов
    document_word_counts = defaultdict(int)  # Счетчик документов, содержащих слово
    documents_words = []  # Список для хранения слов каждого документа

    # Собираем статистику по словам
    for doc in documents:
        words = doc.split()  # Разбиваем документ на слова
        documents_words.append(words)  # Добавляем слова документа в общий список
        for word in set(words):  # Используем set для учета уникальных слов в документе
            vocabulary.add(word)  # Добавляем слово в словарь
            document_word_counts[word] += 1  # Увеличиваем счетчик документов для слова

    # Сортируем словарь для единообразия
    vocabulary = sorted(vocabulary)
    word_to_index = {word: idx for idx, word in enumerate(vocabulary)}  # Создаем отображение слова в индекс
    total_documents = len(documents)  # Общее количество документов

    # Инициализация TF-IDF матрицы
    tfidf_matrix = []

    # Заполнение матрицы TF-IDF
    for words in documents_words:
        # Вычисляем TF (term frequency)
        term_frequency = defaultdict(float)
        words_count = len(words)
        for word in words:
            term_frequency[word] += 1 / words_count  # Нормализованная частота слова

        # Создаем вектор для документа
        document_vector = [0.0] * len(vocabulary)
        for word, tf_value in term_frequency.items():
            # Вычисляем IDF (inverse document frequency)
            inverse_document_frequency = math.log(total_documents / (1 + document_word_counts[word]))
            # Записываем TF-IDF значение в вектор
            document_vector[word_to_index[word]] = tf_value * inverse_document_frequency

        tfidf_matrix.append(document_vector)

    return tfidf_matrix, vocabulary


# Строим TF-IDF матрицу
tfidf_matrix, vocabulary = build_tfidf_matrix(processed_sentences)


# Функция вычисления косинусного расстояния
def cosine_distance(vector1, vector2):
    """
    Вычисляет косинусное расстояние между двумя векторами
    Args:
        vector1: первый вектор
        vector2: второй вектор
    Returns:
        косинусное расстояние (1 - косинусная схожесть)
    """
    # Вычисляем скалярное произведение
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    # Вычисляем нормы векторов
    norm1 = math.sqrt(sum(v * v for v in vector1))
    norm2 = math.sqrt(sum(v * v for v in vector2))
    # Возвращаем косинусное расстояние (1 - косинусная схожесть)
    return 1 - (dot_product / (norm1 * norm2)) if norm1 and norm2 else 1.0


# Создаем список всех возможных пар документов
document_pairs = []
total_documents = len(sentences)
# Используем combinations для создания всех уникальных пар индексов
for i, j in combinations(range(total_documents), 2):
    distance = cosine_distance(tfidf_matrix[i], tfidf_matrix[j])
    document_pairs.append((i, j, distance))

# Сортируем пары по возрастанию расстояния (от наиболее похожих к наименее)
document_pairs.sort(key=lambda x: x[2])


# Функция кластеризации документов
def cluster_documents(document_pairs, num_clusters=3, top_pairs=25):
    """
    Кластеризует документы на основе их косинусного расстояния
    Args:
        document_pairs: список пар документов с расстояниями
        num_clusters: желаемое количество кластеров
        top_pairs: количество наиболее похожих пар для анализа
    Returns:
        список кластеров (каждый кластер - множество индексов документов)
    """
    # Выбираем топ-N наиболее похожих пар
    selected_pairs = document_pairs[:top_pairs]

    # Создаем граф связей между документами
    document_graph = defaultdict(set)
    for i, j, _ in selected_pairs:
        document_graph[i].add(j)
        document_graph[j].add(i)

    # Инициализация структур для кластеризации
    clusters = []
    visited_documents = set()

    # Обход графа для выделения кластеров
    for document_idx in range(total_documents):
        if document_idx not in visited_documents:
            # Создаем новый кластер
            current_cluster = set()
            stack = [document_idx]

            # Обход в глубину для нахождения связанных документов
            while stack:
                current_document = stack.pop()
                if current_document not in visited_documents:
                    visited_documents.add(current_document)
                    current_cluster.add(current_document)
                    # Добавляем всех соседей в стек
                    stack.extend(document_graph[current_document] - visited_documents)

            clusters.append(current_cluster)

    # Объединяем кластеры, пока их количество не станет равным num_clusters
    while len(clusters) > num_clusters:
        # Ищем два ближайших кластера
        min_distance = float('inf')
        clusters_to_merge = (0, 1)

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                # Вычисляем среднее расстояние между кластерами
                total_distance = 0
                pair_count = 0
                for doc_a in clusters[i]:
                    for doc_b in clusters[j]:
                        # Ищем расстояние между текущей парой документов
                        for pair in document_pairs:
                            if (doc_a == pair[0] and doc_b == pair[1]) or (doc_a == pair[1] and doc_b == pair[0]):
                                total_distance += pair[2]
                                pair_count += 1
                                break
                # Вычисляем среднее расстояние, если нашли пары
                if pair_count > 0:
                    average_distance = total_distance / pair_count
                    if average_distance < min_distance:
                        min_distance = average_distance
                        clusters_to_merge = (i, j)

        # Объединяем два ближайших кластера
        if min_distance != float('inf'):
            i, j = clusters_to_merge
            clusters[i].update(clusters[j])
            del clusters[j]
        else:
            break  # Если не нашли пары для объединения, прерываем цикл

    return clusters


# Выполняем кластеризацию
document_clusters = cluster_documents(document_pairs)

# Выводим результаты кластеризации
print("Результаты кластеризации:")
for cluster_num, cluster in enumerate(document_clusters):
    print(f"\nКластер {cluster_num + 1}:")
    for doc_idx in sorted(cluster):
        # Нумерация документов начинается с 1 для удобства чтения
        print(f"{doc_idx + 1}: {sentences[doc_idx]}")