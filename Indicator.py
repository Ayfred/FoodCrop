from enum import Enum

from Describable import Describable
from  Unit import Unit
from IndicatorGroup import IndicatorGroup

## En cours de construction
class Indicator(Describable):


    def __init__(self, id, frequency, freqDesc, geogLocation, indicatorGroup, unit):
        self.id = id
        self.frequency = frequency
        self.freqDesc = freqDesc
        self.geoLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit

    def describe(self):
        return "Indicator, id: " + self.id + "is a " + self.indicatorGroup + ", frequency id : " + self.frequency\
               + ", " + self.freqDesc + ", " + "\n" +  self.unit.describe()


