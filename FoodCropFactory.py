import Commodity
import Indicator
import Measurement
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
import Unit

class FoodCropFactory:

    unit : Unit
    commodity : Commodity
    indicator : Indicator
    measurement : Measurement

    def __init__(self):
        self.Unit = Unit
        self.Commidity = Commodity
        self.Indicator = Indicator
        self.Measurement = Measurement

    def createVolume(self, id):
        self.Unit.Volume(id, "Volume")

    def createPrice(self, id):
        self.Unit.Price(id, "Price")

    def createWeight(self, id, weight):
        self.Unit.Weight(id, "Weight")

    def createSurface(self, id):
        self.Unit.Surface(id, "Surface")

    def createCount(self, id, what):
        self.Unit.Count(id, "Count", what)

    def createRatio(self, id):
        self.Unit.Ratio(id, "Ratio")

    def createCommodity(self, group : CommodityGroup, id, name):
        Commodity(group, id, name)

    def createIndicator(self, id, frequency, freqDesc, geogLocation, indicatorGroup: IndicatorGroup):
        Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, self.Unit)

    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity: Commodity, indicator: Indicator):
        Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
