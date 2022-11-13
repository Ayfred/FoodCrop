from Commodity import Commodity
from Describable import Describable
from Indicator import Indicator


class Measurement(Describable):

    def __init__(self, id: int, year, value: float, timeperiodId: int, timePeriodDesc, Commodity, Indicator):
        self.id = id
        self.year = year
        self.value = value
        self.timeperiodId = timeperiodId
        self.timePeriodDesc = timePeriodDesc
        self.commodity = Commodity
        self.indicator = Indicator

    def describe(self):
        return "Measurement id : " + self.id + " made in " + self.year + " on  " + self.timePeriodDesc \
               + "\n" +  self.commodity.describe() + "\n" + self.indicator.describe()

    def getPeriod(self, id):
        match id:
            case 1:
                return "monthly"
            case 2:
                return "quarterly"
            case 3:
                return "annually"
