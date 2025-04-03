import math


# Функция для вычисления косинусного расстояния между двумя векторами
def cosine_distance(vec1, vec2):
    # Вычисляем скалярное произведение векторов
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

    # Вычисляем нормы векторов
    norm1 = math.sqrt(sum(v ** 2 for v in vec1))
    norm2 = math.sqrt(sum(v ** 2 for v in vec2))

    # Вычисляем косинусную близость
    if norm1 == 0 or norm2 == 0:
        return 1.0  # Если один из векторов нулевой, считаем расстояние максимальным
    cosine_sim = dot_product / (norm1 * norm2)

    # Косинусное расстояние = 1 - косинусная близость
    return 1 - cosine_sim


# Создаем матрицу косинусных расстояний
n_docs = len(vector_model)
distances = [[0.0] * n_docs for _ in range(n_docs)]

# Заполняем матрицу расстояний
for i in range(n_docs):
    for j in range(i, n_docs):
        if i == j:
            distances[i][j] = 0.0  # Расстояние между документом и самим собой = 0
        else:
            dist = cosine_distance(vector_model[i], vector_model[j])
            distances[i][j] = dist
            distances[j][i] = dist  # Матрица симметрична

print("Матрица косинусных расстояний (первые 5 строк):")
for row in distances[:5]:
    print([round(x, 3) for x in row[:5]])