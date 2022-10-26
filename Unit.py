from abc import ABC, abstractmethod
from Describable import Describable


class Unit(Describable, ABC):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def describe(self):
        return self.id, self.name

class Volume(Unit):
    def _init_(self, id, name):
        super().__init__(id, name)

    def describe(self):
        return self.id, self.name

class Weight(Unit):
## En plus des autres constructeurs, on instancie dans celui-là un multiplicateur
    def _init_(self, id, name, multiplier):
        super().__init__(id, name)
        self.multiplier = multiplier

    def describe(self):
        return self.id, self.name, self.multiplier

class Ratio(Unit):
    def _init_(self, id):
        super().__init__(id, "Ratio")

    def describe(self):
        return self.name + self.id

class Price(Unit):
    def _init_(self, id):
        super().__init__(id, "Price")

    def describe(self):
        return self.id, self.name

class Count(Unit):
    def _init_(self, id, what):
        super().__init__(id, "Count")
        self.what = what

    def describe(self):
        return self.id, self.name, self.what

class Surface(Unit):
    def _init_(self, id, name):
        super().__init__(id, "Surface")

    def describe(self):
        return self.id, self.name
