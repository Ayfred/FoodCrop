from Describable import Describable


class Commodity(Describable):

    ## Constructeur
    def __init__(self, commodityGroup, id, name):
        self.id = id
        self.group = commodityGroup
        self.name = name

    ## Méthode describe, on entre les paramètres qu'on souhaite faire afficher
    def describe(self):
        return "Commodity :  id = " + str(self.id) + ", " + self.name + ", group : " + str(self.group)
