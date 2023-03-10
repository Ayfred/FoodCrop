from abc import ABC
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
        return "Volume unit, id : " + str(self.id)

class Weight(Unit):
    def __init__(self, id, multiplier):
        super().__init__(id, "Weight")
        self.multiplier = multiplier

    def describe(self):
        return "Weight unit, id : " + str(self.id) + " which is " + self.multiplier + " kg"


class Ratio(Unit):
    def __init__(self, id, numerateur, denominateur):
        super().__init__(id, "Ratio")
        self.numerateur = numerateur
        self.denominateur = denominateur

    def describe(self):
        return "Ratio unit, id : " + str(self.id) + " numerateur : " + self.numerateur.describe() \
               + " denumerateur : " + self.denominateur.describe()


class Price(Unit):
    def __init__(self, id):
        super().__init__(id, "Price")

    def describe(self):
        return "Price unit, id : " + str(self.id)

class Count(Unit):
    def _init_(self, id, what):
        super().__init__(id, "Count")
        self.what = what

    def describe(self):
        return "Count unit, id : " + str(self.id) + " of " + self.what

class Surface(Unit):
    def __init__(self, id):
        super().__init__(id, "Surface")

    def describe(self):
        return "Surface unit, id : " + self.id
