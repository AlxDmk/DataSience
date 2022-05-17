# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

lst = [random.randint(1, 100) for i in range(20)]
min_ = max_ = sm = 0
for i in lst:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i
for i in lst[min_ + 1:max_]:
    sm += i
print(sm)