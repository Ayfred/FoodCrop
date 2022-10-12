from Commodity import Commodity
from Indicator import Indicator


class Measurement:
    year = int
    value = float
    timeperiodId = int
    timeperiodDescr = str

    def __init__(self, id: int, value: float, timeperiodId : int, timePeriodDesc: str, commodity : Commodity, indicator: Indicator):
        pass


