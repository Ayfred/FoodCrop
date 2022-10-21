from Commodity import Commodity
from CommodityGroup import CommodityGroup
from Indicator import Indicator
from Measurement import Measurement
from Unit import Volume, Price, Weight, Surface, Count, Ratio


class FoodCropFactory:

    def __init__(self):
        self.commodityDico = {}
        self.indicatorDico = {}
        self.unitDico = {}

    def createVolume(self, id):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Volume(id)
        return self.unitDico[str(id)]

    def createPrice(self, id):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Price(id)
        return self.unitDico[str(id)]

    def createWeight(self, id, weight):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Weight(id, weight)
        return self.unitDico[str(id)]

    def createSurface(self, id):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Surface(id)
        return self.unitDico[str(id)]

    def createCount(self, id, what):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Count(id, what)
        return self.unitDico[str(id)]

    def createRatio(self, id):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Ratio(id)
        return self.unitDico[str(id)]

    def createCommodity(self, id, name):
        if id in self.commodityDico:
            return self.commodityDico[str(id)]
        self.commodityDico[str(id)] = Commodity(id, name)
        return self.commodityDico[str(id)]

    def createIndicator(self, id, frequency, freqDesc, geogLocation, indicatorGroup):
        if id in self.indicatorDico:
            return self.indicatorDico[str(id)]
        self.indicatorDico[str(id)] = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup)
        return self.indicatorDico[str(id)]

    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity, indicator):
        return Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)



