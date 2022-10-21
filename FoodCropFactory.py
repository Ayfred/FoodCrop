from Commodity import Commodity
from CommodityGroup import CommodityGroup
from Indicator import Indicator
from Measurement import Measurement
from Unit import Volume, Price, Weight, Surface, Count, Ratio


class FoodCropFactory:

    def createVolume(self, id):
        return Volume(id, "Volume")

    def createPrice(self, id):
        return Price(id, "Price")

    def createWeight(self, id, weight):
        w = Weight(id, "Weight")
        w.multiplier = weight
        return w

    def createSurface(self, id):
        return Surface(id, "Surface")

    def createCount(self, id, what):
        c = Count(id, "Count")
        c.what = what
        return c

    def createRatio(self, id):
        return Ratio(id, "Ratio")

    def createCommodity( self, id, dico, name):
        if id in dico:
            return dico[id]

        dico[str(id)] = Commodity(id, name)
        print(dico[str(id)])
        return dico[str(id)]

    def createIndicator(self, id, frequency, freqDesc, geogLocation, IndicatorGroup):
        return Indicator(id, frequency, freqDesc, geogLocation, IndicatorGroup)

    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity, indicator):
        return Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)



