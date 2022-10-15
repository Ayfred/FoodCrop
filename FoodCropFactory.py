import Commodity
import Indicator
import Measurement
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
import Unit

class FoodCropFactory:
    def __init__(self):
        self.Unit = Unit
        self.Commidity = Commodity
        self.Indicator = Indicator

    def createVolume(self, id):
        return self.Unit.Volume(id, "Volume")

    def createPrice(self, id):
        return self.Unit.Price(id, "Price")

    def createWeight(self, id, weight):
        return self.Unit.Weight(id, "Weight")

    def createSurface(self, id):
        return self.Unit.Surface(id, "Surface")

    def createCount(self, id, what):
        #return self.Unit.Count(id, "Count", what)
        pass

    def createRatio(self, id):
        return self.Unit.Ratio(id, "Ratio")

    def createCommodity(group : CommodityGroup, id, name):
        return Commodity.Commodity(group, id, name)

    def createIndicator(self, id, frequency, freqDesc, geogLocation, indicatorGroup: IndicatorGroup):
        return Indicator.Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, self.Unit)

    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity: Commodity, indicator: Indicator):
        return Measurement.Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)



