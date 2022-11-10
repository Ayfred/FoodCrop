from CommodityGroup import CommodityGroup
from Describable import Describable


class Commodity(Describable):

    def __init__(self, commodityGroup, id, name):
        self.id = id
        self.group = commodityGroup
        self.__name = name

    def describe(self):
        return "Commodity :  id = " + self.id + ", It's a" + self.name + " which is in the group" + self.group
