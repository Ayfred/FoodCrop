from CommodityGroup import CommodityGroup
from Describable import Describable


class Commodity(Describable):

    def describe(self):
        pass

    def __init__(self, commodityGroup, id, name):
        self.id = id
        self.group = commodityGroup
        self.__name = name

    def describe(self):
        pass
