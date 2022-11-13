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
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Volume(id)
        Volume.describe(Volume(id))
        return self.unitDico[str(id)]

    ## Création des prix
    def createPrice(self, id):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Price(id)
        return self.unitDico[str(id)]

    ## Création des poids
    def createWeight(self, id, weight):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Weight(id, weight)
        return self.unitDico[str(id)]

    ##Création de surfaces
    def createSurface(self, id):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Surface(id)
        return self.unitDico[str(id)]

    ##Création d'un paramètre de comptage
    def createCount(self, id, what):
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Count(id, what)
        return self.unitDico[str(id)]

    ##Création d'un paramètre de ratio
    def createRatio(self, id):
        """ Un ratio est une fabrication de deux autres unités,
        on les ajoutes donc comme attribut du ratio que l'on créé
        """
        match(id):
            case 4:
                numerateur = self.createPrice(47, "Dollars")
                denominateur = self.createVolume(3, "Bushels")
            case 5:
                numerateur = self.createPrice(47, "Dollars")
                denominateur = self.createWeight(48, "CRW", 50.80)
            case 6:
                numerateur = self.createVolume(3, "Bushels")
                denominateur = self.createSurface(49, "Acre")
            case 11:
                numerateur = self.createWeight(41, "Ton", 907.185)
                denominateur = self.createSurface(49, "Acre")
            case 12:
                numerateur = self.createPrice(47, "Dollars")
                denominateur = self.createWeight(41, "Ton", 907.185)
            case 13:
                numerateur = self.createCount(50, "Unidentifiable", "unidentifiable part of a ratio")
                denominateur = self.createCount(50, "Unidentifiable", "unidentifiable part of a ratio")
            case 14:
                numerateur = self.createPrice(51, "Cents")
                denominateur = self.createWeight(52, "Pound", 0.454)
            case 31:
                numerateur = self.createPrice(47, "Dollars")
                denominateur = self.createWeight(41, "Ton", 907.185)
            case 45:
                numerateur = self.createWeight(53, "Metric tons", 1000.)
                denominateur = self.createSurface(54, "Hectare")

        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Ratio(id, numerateur, denominateur)
        return self.unitDico[str(id)]

    ## On va collecter les produits grâce à leurs identifiants : si les id sont dans le dictionnaire alors on retourne la donnée en String
    def createCommodity(self,commodityGroup,  id, name):
        if id in self.commodityDico:
            return self.commodityDico[str(id)]
        self.commodityDico[str(id)] = Commodity(commodityGroup, id, name)
        return self.commodityDico[str(id)]

    ##Création d'un indicateur prenant en argument un identifiant, une fréquence, une description de fréquence une localisation GPS, etc.
    ##On fait appel au dictionnaire Indicator. Si un id se trouve dans le dico, la méthode renvoie le Indicator en string
    def createIndicator(self, id, frequency, freqDesc, geogLocation, indicatorGroup, unit):
        if id in self.indicatorDico:
            return self.indicatorDico[str(id)]
        self.indicatorDico[str(id)] = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)
        return self.indicatorDico[str(id)]

    ## Création de mesures
    ## La méthode retourne un tuple contenant un id, une valeur, une période de temps, sa description, le produit sur lequel s'applique la mesure et un indicateur choisi pour la mesure.
    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity, indicator):
        return Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)

    def createUnit(self, id, name):
        if id in self.unitDico:
            return self.indicatorDico[str(id)]
        #match ne marche que pour Python 3.10 ou ultérieure
        match id:
            case 4 | 5 | 6 | 11 | 12 | 13 | 14 | 31 | 45:
                return self.createRatio(id)
            case 7 | 8 | 9 | 41:
                return self.createWeight(id, self.getMultiplier(id))
            case 1 | 3 | 17 | 18:
                return self.createVolume(id)
            case 2 | 10 | 44:
                return self.createSurface(id)
            case 15:
                return self.createPrice(id)
            case 16 | 46:
                return self.createCount(id, name)

    def getMultiplier(self, id):
        match id:
            case 7:
                return 1000000.
            case 8:
                return 10**9.
            case 9:
                return 907185.
            case 41:
                return 907.185

