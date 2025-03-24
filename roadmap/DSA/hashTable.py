from collections import Counter
import pprint


# Хэш таблицы

# В этом примере хэш-функция берет строку, суммирует ASCII-коды всех символов и берет остаток от деления на 10. Это
# простой, но эффективный способ преобразования строки в числовое значение.
def simple_hash(key):
    return sum(ord(char) for char in key) % 10


# линейное пробивание
def linear_probing(hash_table, key, value):
    index = simple_hash(key)
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
    hash_table[index] = (key, value)
    return hash_table


# квадратичное пробивание
def quadratic_probing(hash_table, key, value):
    index = simple_hash(key)
    i = 1
    while hash_table[index] is not None:
        index = (index + i ** 2) % len(hash_table)
        i += 1
    hash_table[index] = (key, value)
    return hash_table


# Задача 1: Подсчет частоты элементов
# Напишите функцию, которая принимает список и возвращает словарь с частотой каждого элемента.

def count_elem(mas):
    result_dict = {}
    for elem in mas:
        if elem in result_dict:
            result_dict[elem] += 1
        else:
            result_dict[elem] = 1
    return result_dict


# так же это можно реализовать через (collections.Counter)
# этот метод быстрее так как сам Counter написан на C
def count_mod(mas):
    count = Counter(mas)
    return count


# Задача 2: Проверка на анаграммы
# Напишите функцию, которая проверяет, являются ли две строки анаграммами
def anagrams(str1, str2):
    return count_mod(str1) == count_elem(str2)


# Задача 3: Поиск двух чисел с заданной суммой
# напишите функцию, которая находит два числа в списке, сумма которых равна заданному значению.
def sum_search(lst, value):
    result_dic = {}
    for item in lst:
        difference = value - item
        if difference in result_dic:
            return (item, difference)
        result_dic[item] = True
    return None


# Проверил скорость выполнения функции со списком и словарём. Вот результат
# Время выполнения: 0.0631848000921309 секунд (список)
# Время выполнения: 0.05525190010666847 секунд (словарь)

# Задача 4: Удаление дубликатов из списка
# Напишите функцию, которая удаляет дубликаты из списка, сохраняя порядок элементов.


test_mas = [None] * 10
numb_list = [1, 4, 2, 3, 4, 1, 2, 3, 3]
string = 'преобразование строки в числовое значение'

print(simple_hash(string))
print(count_elem(numb_list), count_mod(numb_list))
print(anagrams('dog', 'dog'))

numbers = [2, 7, 11, 15]
target = 9

print(sum_search(numbers, target))
print(count_elem(numb_list).keys())
pprint.pprint(linear_probing(test_mas, string, 2))
print(quadratic_probing(test_mas, string, 3))
