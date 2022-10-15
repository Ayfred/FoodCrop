from abc import ABC, abstractmethod

class Unit(ABC):

    def __init__(self, id, name):
        self.id = id
        self.name = name



class Volume(Unit):

    def _init_(self, id, name):
        super().__init__(id, "Volume")

class Weight(Unit):

    def _init_(self, id, name, multiplier):
        super().__init__(id, "Weight")
        self.multiplier = multiplier

class Ratio(Unit):

    def _init_(self, id, name):
        super().__init__(id, "Ratio")

class Price(Unit):

    def _init_(self, id, name):
        super().__init__(id, "Price")

class Count(Unit):
    def _init_(self, id, name,what):
        super().__init__(id, "Count")
        self.what = what

class Surface(Unit):

    def _init_(self, id, name):
        super().__init__(id, "Surface")
