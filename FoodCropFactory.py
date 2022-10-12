import Commodity
import Indicator
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
import Unit

class FoodCropFactory:

    def __init__(self):
        pass


    def createVolume(self, id):
        pass

    def createPrice(self, id):
        pass

    def createWeight(self, id, weight):
        pass

    def createSurface(self, id):
        pass

    def createCount(self, id, what):
        pass

    def createRatio(self, id):
        pass

    def createCommodity(self, group : CommodityGroup, id, name):
        pass

    def createIndicator(self, id, frequency, freqDesc, geogLocation, indicatorGroup: IndicatorGroup):
        pass

    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity: Commodity, indicator: Indicator):
        pass
