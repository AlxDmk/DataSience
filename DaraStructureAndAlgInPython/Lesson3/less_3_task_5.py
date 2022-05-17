# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

lst = [random.randint(-999, 20) for _ in range(20)]
min_ = float('-inf')
for i in lst:
    if min_ < i < 0:
        min_ = i
print(min_)