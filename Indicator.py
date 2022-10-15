from enum import Enum
from  Unit import Unit
from IndicatorGroup import IndicatorGroup


class Indicator:
    def __init__(self, id, frequency, freqDesc, geogLocation, IndicatorGroup):
        self.id = id
        self.__frequency = frequency
        self.__freqDesc = freqDesc
        self.__geoLocation = geogLocation
        self.indicatorGroup = IndicatorGroup
        self.unit = Unit

