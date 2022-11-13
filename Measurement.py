from Describable import Describable

class Measurement(Describable):

    ## Constructeur
    def __init__(self, id: int, year, value: float, timeperiodId: int, timePeriodDesc, Commodity, Indicator):
        self.id = id
        self.year = year
        self.value = value
        self.timeperiodId = timeperiodId
        self.timePeriodDesc = timePeriodDesc
        self.commodity = Commodity
        self.indicator = Indicator

    ## Méthode describe, on entre les paramètres qu'on souhaite faire afficher
    def describe(self):
        return ("Measurement id : " + str(self.id) + " made in " + str(self.year) + " on  " + self.timePeriodDesc \
                + ", id timePeriod: " + str(self.timeperiodId) + "\n" + self.commodity.describe() + "\n"
                + self.indicator.describe()) + "\n"
