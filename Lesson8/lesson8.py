# ----------------1. ---------------------
import re


class Data:

    def __init__(self, data):
        pattern = r'[0-3][0-9]-[0-1][0-9]-[1-2]([0-9]{3})'

        if re.fullmatch(pattern, data):
            print("Данные получены в верном формате")
            self.get_numbers(data)
        else:
            raise Exception("Данные предоставлены в неверном формате!")

    @classmethod
    def get_numbers(cls, data):
        print("Литеры преобразованы в цифры")
        cls.check_numbers([int(n) for n in data.split('-')])

    @staticmethod
    def check_numbers(list):
        if not 0 < list[0] <= 31 or not 0 < list[1] < 13 or not 1000 <= list[2] <= 2999:
            raise Exception("Данные не календарного формата")
        print(f'Всё в порядке! Формат даты корректен! День: {list[0]} Месяц: {list[1]} Год: {list[2]}')


my_data = Data(input("Введите дату: "))


# ----------------2. ---------------------
class MyZeroDevisionEx(Exception):
    def __str__(self):
        return "Вы пытаетесь разделить на ноль!"


a = 6
b = int(input('Введите делимое '))
try:
    if b == 0:
        raise MyZeroDevisionEx()
    print(f"Результат: {a / b}")
except MyZeroDevisionEx as err:
    print(err)


# ----------------3. ---------------------
class OnlyNumbersEx(Exception):
    def __str__(self):
        return "Данные должны быть только числа"


result_list = []
while True:
    data = input('Введите данные ')
    if data == 'stop':
        break
    try:
        if not data.isdigit():
            raise OnlyNumbersEx()
        result_list.append(int(data))
    except OnlyNumbersEx as err:
        print(err)

print(result_list)


##################################################
# Задания 4, 5, 6 Реализованы в отдельном проекте#
# ################################################

# ----------------7. ---------------------
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+i{self.b}'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex((self.a * other.a) - (self.b * other.b), (self.a * other.b + other.a * self.b))


my_complex1 = Complex(1, 2)
print(my_complex1)
my_complex2 = Complex(2, 1)
print(my_complex1 + my_complex2)
print(my_complex1 * my_complex2)