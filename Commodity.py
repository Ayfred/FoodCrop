from CommodityGroup import CommodityGroup
class Commodity:

    def __init__(self,group: CommodityGroup, id: str, name: str):
        self.id = id
        self.group = group
        self.name = name



