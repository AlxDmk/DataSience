import MyExceptions as ex


def performance_checker(func):
    def wrapper(self, *args):
        try:
            if not self.is_ready:
                raise ex.MyEqpmtExploiteEx(f"{self.type} invN: {self.inv} is broken!")
            func(self, *args)
        except ex.MyEqpmtExploiteEx as err:
            print(err)

    return wrapper


def command_checker(func):
    def wrapper(self, command, *data):
        try:
            if command not in self.funcs:
                raise ex.MyEqpmtAbilityEx()
            func(self, command, *data)
        except ex.MyEqpmtAbilityEx as err:
            print(err)

    return wrapper


def capacity_checker(func):
    def wrapper(self, other):
        try:
            if other in self.storage:
                raise ex.MyInventoryEx()
            if self.capacity < 0:
                raise ex.MyCapacityEx(f"Not enough space for storage in {self.name}")
            func(self, other)
        except ex.MyInventoryEx as err:
            print (err)
        except ex.MyCapacityEx as err:
            print(err.text)
    return wrapper
