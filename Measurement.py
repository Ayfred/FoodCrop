from Commodity import Commodity
from Indicator import Indicator


class Measurement:
    year = int
    value = float
    timeperiodId = int
    timeperiodDescr = str

    def __init__(self, id: int, year, value: float, timeperiodId : int, timePeriodDesc: str, commodity : Commodity, indicator: Indicator):
        self.id = id
        self.year = year
        self.value = value
        self.timeperiodId = timeperiodId
        self.timePeriodDesc = timePeriodDesc
        self.commidity = commodity
        self.indicator = indicator



