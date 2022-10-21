from CommodityGroup import CommodityGroup
from Describable import Describable


class Commodity(Describable):

    def describe(self):
        pass

    def __init__(self, id, name):
        self.id = id
        self.group = CommodityGroup
        self.__name = name



