# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
min_ = max_ = 0
lst = [random.randint(-90, 90) for _ in range(20)]

for i in lst:
    if i < min_:
        min_ = i
    if i > max_:
        max_ = i

lst[lst.index(min_)], lst[lst.index(max_)] = lst[lst.index(max_)], lst[lst.index(min_)]
print(lst)