data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

def calculate_structure_sum(*args):
    sum = 0
    for i in args:
        if isinstance(i, (list, tuple, set)):
            sum += calculate_structure_sum(*i)
        elif isinstance(i, str):
            sum += len(i)
        elif isinstance(i, (int, float)):
            sum += i
        elif isinstance(i, dict):
            sum += calculate_structure_sum(*i.items())
    return sum


result = calculate_structure_sum(data_structure)
print(result)