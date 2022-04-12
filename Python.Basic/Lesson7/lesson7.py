# # -------------- 1. ------------------------
class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        graph = ""
        for row in self.data:
            graph += "{}\n".format('\t'.join(map(str, row)))
        return graph

    def __add__(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(result)


my_matrix = Matrix([[1, 2, 3], [3, 4, 6], [5, 6, 9]])
my_matrix2 = Matrix([[3, 4, 7], [9, 6, 7], [1, 2, 3]])
print(my_matrix + my_matrix2)

# -------------- 2. ------------------------
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.__v = v

    def __add__(self, other):
        return self.consumption + other.cosumption

    @property
    def consumption(self):
        return self.__v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.__h = h

    def __add__(self, other):
        return self.consumption + other.cosumption

    @property
    def consumption(self):
        return 2 * self.__h + 0.3


my_coat = Coat(150)
my_suit = Suit(100)
print(my_suit.consumption + my_coat.consumption)


# -------------- 3. ------------------------

class Cell:
    def __init__(self, els):
        self.els = els

    def __add__(self, other):
        return Cell(self.els + other.els)

    def __sub__(self, other):
        return self.els - other.els if self.els - other.els > 0 else "Сообщение об ошибке"

    def __mul__(self, other):
        return Cell(self.els * other.els)

    def __truediv__(self, other):
        return Cell(self.els // other.els)

    def make_order(self, count, tail=""):
        return '\n'.join(["*" * count for i in range(self.els // count)] + ["*" * (self.els % count)])


my_cell = Cell(13)
my_cell2 = Cell(7)

print(my_cell.make_order(6))
print(my_cell2.make_order(8))
