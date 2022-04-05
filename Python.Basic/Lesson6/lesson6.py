import time
from itertools import cycle
from functools import reduce


# --------- 1.------------------
class TrafficLight:
    color = ['Red', 'Yellow', 'Green', 'Yellow']

    def __init__(self):
        self.running()

    def running(self):
        timing = [7, 3, 5, 3]
        result = list(zip(TrafficLight.color, timing))
        iter = int(input("Количество итераций "))
        c = 0
        for el in cycle(result):
            if c > iter:
                break
            print(el[0])
            time.sleep(el[1])
            c += 1


my_tl = TrafficLight()


# --------- 2.------------------
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self, depth):
        mass = 25
        return self._length * self._width * mass * depth


my_road = Road(20, 5000)
print(my_road.calculate(5))


# --------- 3.------------------
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"ФИО: {self.name} {self.surname}"

    def get_total_income(self):
        return reduce(lambda x, y: x + y, self._income.values())


my_position = Position('Alx', 'Dmk', 'manager', 1000, 500)
print(my_position.get_full_name())
print(my_position.get_total_income())


# --------- 4.------------------
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        a = 'Это полицейская машина.' if self.is_police else 'Это не полицейская машина.'
        print(f" {self.name} {self.color} Начала движение. {a}")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {self.direction} ")

    def show_speed(self):
        print(f"Машина двигается со скростью {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Превышена максимальная скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышена максимальная скорость!")


class PoliceCar(Car):
    pass


my_work_car = WorkCar(60, 'yellow', 'Work car', False)
my_work_car.show_speed()

my_police_car = PoliceCar(90, "White", 'Police', True)
my_police_car.go()


# --------- 5.------------------
class Stationery:
    title = None

    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Шариковая {self.title} пишет чернилами")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} рисует в альбоме")


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} отмечает интересный текст')


my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')
