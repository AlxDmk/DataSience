from sys import argv
from functools import reduce
import itertools

# --------------------1. ---------------------
script_name, hours_worked, rate_per_hour, premium = argv


def payroll():
    try:
        return int(hours_worked) * int(rate_per_hour) + int(premium)
    except(ValueError, TypeError) as error:
        return error


print('Заработная плата составила: ', payroll())

# ------------------ 2. ----------------------
list_ = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [n for n, k in zip(list_[1:], list_) if k < n]

# ------------------ 3.-----------------------
result = [n for n in range(20, 241) if bool(n % 20) != bool(n % 21)]

# -------------------4.-----------------------
list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [n for n in list_1 if list_1.count(n) == 1]


# -------------------5. ----------------------
def multiply(el_1, el_2):
    return el_1 * el_2


list_1 = [n for n in range(100, 1001) if not (n % 2)]
result = reduce(multiply, list_1)

# ----------------- 6. ------------------------
# ● итератор, генерирующий целые числа, начиная с указанного;
counter = itertools.count(3)
el = 0
while el < 10:
    el = (next(counter))
    print(el)

# или

l = itertools.islice(itertools.count(3), 8)
for el in l:
    print(el)

# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
l = itertools.islice(itertools.cycle('ABC'), 10)
for el in l:
    print(el)


# ---------------- 7.--------------------------
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
        yield factorial


def func(n):
    for element in fact(n):
        print(element, end=", ")


func(5)
