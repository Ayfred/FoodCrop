from abc import ABC, abstractmethod
from Describable import Describable


class Unit(Describable, ABC):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def describe(self):
        pass

class Volume(Unit):
    def _init_(self, id, name):
        super().__init__(id, name)

    def describe(self):
        pass

class Weight(Unit):

    def _init_(self, id, name, multiplier):
        super().__init__(id, name)
        self.multiplier = multiplier

    def describe(self):
        pass

class Ratio(Unit):
    def _init_(self, id):
        super().__init__(id, "Ratio")

    def describe(self):
        print(self.name + self.id)

class Price(Unit):
    def _init_(self, id):
        super().__init__(id, "Price")

    def describe(self):
        pass

class Count(Unit):
    def _init_(self, id, what):
        super().__init__(id, "Count")
        self.what = what

    def describe(self):
        pass

class Surface(Unit):
    def _init_(self, id, name):
        super().__init__(id, "Surface")

    def describe(self):
        pass
