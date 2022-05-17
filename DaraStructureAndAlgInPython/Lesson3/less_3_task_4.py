# 4. Определить, какое число в массиве встречается чаще всего.
import random

max_ = 0
num_ = []
lst = [random.randint(1, 10) for _ in range(20)]
set_ = set(lst)
for s in set_:
    if lst.count(s) > max_:
        num_ = []
        max_ = lst.count(s)
        num_.append(s)
    elif lst.count(s) == max_:
        num_.append(s)

print(f'{num_}: {max_}')