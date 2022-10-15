from Commodity import Commodity
from Describable import Describable
from Indicator import Indicator


class Measurement(Describable):
    year = int
    value = float
    timeperiodId = int
    timeperiodDescr = str

    def __init__(self, id: int, year, value: float, timeperiodId : int, timePeriodDesc, Commodity, Indicator):
        self.id = id
        self.__year = year
        self.__value = value
        self.__timeperiodId = timeperiodId
        self.__timePeriodDesc = timePeriodDesc
        self.commidity = Commodity
        self.indicator = Indicator



