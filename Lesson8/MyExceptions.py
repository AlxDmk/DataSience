class MyEqpmtExploiteEx(Exception):
    def __init__(self, text):
        self.text = text


class MyEqpmtAbilityEx(Exception):
    def __str__(self):
        return 'I can not execute this operation !'


class MyCapacityEx(Exception):
    def __init__(self, text):
        self.text = text


class MyInventoryEx(Exception):
    def __str__(self):
        return "This item is already in stock"
