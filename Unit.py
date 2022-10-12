from abc import ABC, abstractmethod

class Unit(ABC):

    id : int
    name : str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    #méthodes abstractes :







class Volume(Unit):

    def _init_(id, name):
        Unit(id, "Volume")

class Weight(Unit):

    def _init_(id, name, multiplier):
        Unit(id, "Weight")

class Ratio(Unit):

    def _init_(id, name):
        Unit(id, "Ratio")

class Price(Unit):

    def _init_(id, name):
        Unit(id, "Price")

class Count(Unit):

    def _init_(id, name,what):
        Unit(id, "Count", what)

class Surface(Unit):

    def _init_(id, name):
        Unit(id, "Surface")
