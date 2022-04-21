# ---------------- 4. -----------------

from abc import ABC, abstractmethod
import decorators as deco
from collections import Counter


class User:
    def __init__(self):
        pass

    @staticmethod
    def set_command(target, command, data):
        target.get_command(command, data)


class Org:
    def __init__(self, inv, resource=2):
        self.resource = resource
        self.inv = inv
        self.type = type(self).__name__

    @deco.command_checker
    def get_command(self, command, data):
        self.working(command, data)

    @deco.performance_checker
    def working(self, command, data):
        print(f"I'm {command} with {data}")
        self.resource -= 1

    @property
    def is_ready(self):
        return True if self.resource > 0 else False


class Printer(Org):
    funcs = ['printing']


class Scanner(Org):
    funcs = ['scanning']


class Fax(Org):
    funcs = ['sending fax', 'receiving fax']


my_printer = Printer(1)
my_scanner = Scanner(2, 1)
my_fax = Fax(2, 2)

# I'm printing with text for printing
User.set_command(my_printer, 'printing', 'text for printing')

# I can not execute this operation !
User.set_command(my_printer, 'scanning', 'text for scanning')

# I'm printing with text for printing
User.set_command(my_printer, 'printing', 'text for printing')

# Printer invN: 1 is broken!
User.set_command(my_printer, 'printing', 'text for printing')

# I'm scanning with data
User.set_command(my_scanner, 'scanning', 'data')

# Scanner invN: 2 is broken!
User.set_command(my_scanner, 'scanning', 'data')


# ---------------- 5. -----------------
class Company:
    def __init__(self, name, capacity=2):
        self.storage = set()
        self.name = name
        self.capacity = capacity

    @deco.capacity_checker
    def __add__(self, other):
        self.storage.add(other)
        self.capacity -= 1
        return self.storage, self.capacity

    @property
    def inventory(self):
        return dict(Counter(n.type for n in self.storage))

    @property
    def enough_place(self):
        return True if self.capacity > 0 else False

    def transfer(self, other, item):
        if item in self.storage and other.enough_place:
            self.storage.remove(item)
            other + item
            self.capacity += 1


class Store(Company):
    def __init__(self, name):
        super().__init__(name)


class Department(Company):
    def __init__(self, name):
        super().__init__(name)


my_store = Store("Store#1")
my_dep = Department("Accounting")
# my_store.transfer(my_dep, my_printer)

my_store + my_printer
my_store + my_scanner
my_store + my_fax

# This item is already in stock
my_store + my_fax

my_store.transfer(my_dep, my_printer)

print(my_store.inventory)
print(my_dep.inventory)
