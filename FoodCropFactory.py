from Commodity import Commodity
from CommodityGroup import CommodityGroup
from Indicator import Indicator
from Measurement import Measurement
from Unit import Volume, Price, Weight, Surface, Count, Ratio


class FoodCropFactory:
    def __init__(self) -> None:
        super().__init__()
        self.commodityDico = {}
        self.indicatorDico = {}
        self.unitDico = {}

    ## Création de volume
    def createVolume(self, id):
        return Volume(id, "Volume")
## Création des prix
    def createPrice(self, id):
        return Price(id, "Price")
## Création des poids
    def createWeight(self, id, weight):
        w = Weight(id, "Weight")
        w.multiplier = weight
        return w
##Création de surfaces
    def createSurface(self, id):
        return Surface(id, "Surface")
    ##Création d'un paramètre de comptage
    def createCount(self, id, what):
        c = Count(id, "Count")
        c.what = what
        return c
##Création d'un paramètre de ratio
    def createRatio(self, id):
        return Ratio(id, "Ratio")
## On va collecter les produits grâce à leurs identifiants : si les id sont dans le dictionnaire alors on retourne la donnée en String
    def createCommodity(self, id, name):
        if id in self.commodityDico:
            return self.commodityDico[str(id)]
        self.commodityDico[str(id)] = Commodity(id, name)
        return self.commodityDico[str(id)]


##Création d'un indicateur prenant en argument un identifiant, une fréquence, une description de fréquence une localisation GPS, etc.
    ##On fait appel au dictionnaire Indicator. Si un id se trouve dans le dico, la méthode renvoie le Indicator en string
    def createIndicator(self, id, frequency, freqDesc, geogLocation, indicatorGroup):
        if id in self.indicatorDico:
            return self.indicatorDico[str(id)]
        self.indicatorDico[str(id)] = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup)
        return self.indicatorDico[str(id)]

## Création de mesures
    ## La méthode retourne un tuple contenant un id, une valeur, une période de temps, sa description, le produit sur lequel s'applique la mesure et un indicateur choisi pour la mesure.
    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity, indicator):
        return Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
