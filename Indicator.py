from Describable import Describable

class Indicator(Describable):

    ## Constructeur
    def __init__(self, id, frequency, freqDesc, geogLocation, indicatorGroup, unit):
        self.id = id
        self.frequency = frequency
        self.freqDesc = freqDesc
        self.geoLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit

    ## Méthode describe, on entre les paramètres qu'on souhaite faire afficher
    def describe(self):
        return "Indicator, id : " + str(self.id) + " is a " + str(self.indicatorGroup) + ", frequency id : " \
               + str(self.frequency) + ", " + self.freqDesc + ", " + "\n" + self.unit.describe()


