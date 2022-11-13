from CommodityGroup import CommodityGroup
from Describable import Describable


class Commodity(Describable):

    def __init__(self, commodityGroup, id, name):
        self.id = id
        self.group = commodityGroup
        self.name = name

    def describe(self):
        return "Commodity :  id = " + str(self.id) + ", " + self.name + ", group : " + str(self.group)
