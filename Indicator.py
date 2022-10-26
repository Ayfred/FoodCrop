from enum import Enum

from Describable import Describable
from  Unit import Unit
from IndicatorGroup import IndicatorGroup

## En cours de construction
class Indicator(Describable):


    def __init__(self, id, frequency, freqDesc, geogLocation, IndicatorGroup):
        self.id = id
        self.__frequency = frequency
        self.__freqDesc = freqDesc
        self.__geoLocation = geogLocation
        self.indicatorGroup = IndicatorGroup
        self.unit = Unit

    def describe(self):
        return self.id, self.__freqDesc
