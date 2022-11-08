from abc import ABC, abstractmethod
from Describable import Describable

## Instanciation de identifiant et nom dans le constructeur
class Unit(Describable, ABC):

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.description = {}

## Permet de rechercher l'identifiant et le nom d'un paramètre (permet d'avoir plus d'infos sur un paramètre)
    def describe(self):
        return self.id, self.name
## Sous-classe de Unit, on fait appel à la méthode super() dans le constructeur afin de souligner l'hérédité
class Volume(Unit):
    def __init__(self, id):
        super().__init__(id, "Volume")

    def describe(self):
        return self.name

class Weight(Unit):
## En plus des autres constructeurs, on instancie dans celui-là un multiplicateur
    def __init__(self, id, multiplier):
        super().__init__(id, "Weight")
        self.multiplier = multiplier

    def describe(self):
        return self.id, self.name, self.multiplier
## Rien ne change pour le reste pour l'instant
class Ratio(Unit):
    def __init__(self, id):
        super().__init__(id, "Ratio")

    def describe(self):
        pass

class Price(Unit):
    def __init__(self, id):
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
    def __init__(self, id):
        super().__init__(id, "Surface")

    def describe(self):
        return self.id, self.name
