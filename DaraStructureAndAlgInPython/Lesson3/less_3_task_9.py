# 9 Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
matrix = []
min_list = []
for _ in range(5):
    lst = [random.randint(-99, 99) for _ in range(5)]
    matrix.append(lst)
for _ in zip(*matrix):
    min_ = float('inf')
    for _ in _:
        if _ < min_:
            min_= _
    min_list.append(min_)   
max_= float('-inf')
for _ in min_list:
    if _ > max_:
        max_ = _
print(min_list)
print(max_)