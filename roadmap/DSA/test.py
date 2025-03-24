import timeit
code_to_test = """
def find_pair_with_sum(lst, target_sum):
    seen = {}
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

# Пример использования
numbers = [2, 7, 11, 15]
target = 9
print(find_pair_with_sum(numbers, target)) """
execution_time = timeit.timeit(code_to_test, number=10000)
print(f"Время выполнения: {execution_time} секунд")

# Время выполнения: 0.0631848000921309 секунд
# Время выполнения: 0.05525190010666847 секунд