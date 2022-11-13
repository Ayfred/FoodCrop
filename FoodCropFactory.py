from Commodity import Commodity
from Indicator import Indicator
from Measurement import Measurement
from Unit import Volume, Price, Weight, Surface, Count, Ratio


class FoodCropFactory:
    def __init__(self) -> None:
        super().__init__()

        ## Création des dictionnaires
        self.commodityDico = {}
        self.indicatorDico = {}
        self.unitDico = {}

    def createVolume(self, id):
        """ On enregistre l'identifiant dans le dictionnaire unitDico
         que si ce dernier n'est pas présent dans le dictionnaire
        """
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Volume(id)
        Volume.describe(Volume(id))
        return self.unitDico[str(id)]

    ## Création des prix
    def createPrice(self, id):
        """ On enregistre l'identifiant dans le dictionnaire unitDico
        que si ce dernier n'est pas présent dans le dictionnaire
        """
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Price(id)
        return self.unitDico[str(id)]

    ## Création des poids
    def createWeight(self, id, weight):
        """ On enregistre l'identifiant dans le dictionnaire unitDico
        que si ce dernier n'est pas présent dans le dictionnaire
        """
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Weight(id, weight)
        return self.unitDico[str(id)]

    ##Création de surfaces
    def createSurface(self, id):
        """ On enregistre l'identifiant dans le dictionnaire unitDico
        que si ce dernier n'est pas présent dans le dictionnaire
        """
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Surface(id)
        return self.unitDico[str(id)]

    ##Création d'un paramètre de comptage
    def createCount(self, id, what):
        """ On enregistre l'identifiant dans le dictionnaire unitDico
        que si ce dernier n'est pas présent dans le dictionnaire
        """
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
                numerateur = self.createPrice(47)
                denominateur = self.createVolume(3)
            case 5:
                numerateur = self.createPrice(47)
                denominateur = self.createWeight(48, 50.80)
            case 6:
                numerateur = self.createVolume(3)
                denominateur = self.createSurface(49)
            case 11:
                numerateur = self.createWeight(41, 907.185)
                denominateur = self.createSurface(49)
            case 12:
                numerateur = self.createPrice(47)
                denominateur = self.createWeight(41, 907.185)
            case 13:
                numerateur = self.createCount(50, "unidentifiable part of a ratio")
                denominateur = self.createCount(50, "unidentifiable part of a ratio")
            case 14:
                numerateur = self.createPrice(51)
                denominateur = self.createWeight(52, 0.454)
            case 31:
                numerateur = self.createPrice(47)
                denominateur = self.createWeight(41, 907.185)
            case 45:
                numerateur = self.createWeight(53, 1000.)
                denominateur = self.createSurface(54)

        ## On enregistre l'identifiant dans le dictionnaire unitDico que si ce dernier n'est pas présent dans le dictionnaire
        if id in self.unitDico:
            return self.unitDico[str(id)]
        self.unitDico[str(id)] = Ratio(id, numerateur, denominateur)
        return self.unitDico[str(id)]

    ## On va collecter les produits grâce à leurs identifiants : si les id sont dans le dictionnaire alors on retourne la donnée en String
    def createCommodity(self,commodityGroup,  id, name):
        """ On enregistre l'identifiant dans le dictionnaire commodityDico
        que si ce dernier n'est pas présent dans le dictionnaire
        """
        if id in self.commodityDico:
            return self.commodityDico[str(id)]
        self.commodityDico[str(id)] = Commodity(commodityGroup, id, name)
        return self.commodityDico[str(id)]

    ##Création d'un indicateur prenant en argument un identifiant, une fréquence, une description de fréquence une localisation GPS, etc.
    ##On fait appel au dictionnaire Indicator. Si un id se trouve dans le dico, la méthode renvoie le Indicator en string
    def createIndicator(self, id, frequency, freqDesc, geogLocation, indicatorGroup, unit):
        """ On enregistre l'identifiant dans le dictionnaire IndicatoDico
        que si ce dernier n'est pas présent dans le dictionnaire
        """
        if id in self.indicatorDico:
            return self.indicatorDico[str(id)]
        self.indicatorDico[str(id)] = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)
        return self.indicatorDico[str(id)]

    ## Création de mesures
    ## La méthode retourne un tuple contenant un id, une valeur, une période de temps, sa description, le produit sur lequel s'applique la mesure et un indicateur choisi pour la mesure.
    def createMeasurement(self, id, year, value, timeperiodId, timeperiodDesc, commodity, indicator):
        return Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)

    def createUnit(self, id, name):
        """ createUnit permet de trouver a partir de l'id de l'unité associé à
        une mesure quel constructeur de sous classe il fautdra appeler
        """
        if id in self.unitDico:
            return self.indicatorDico[str(id)]
        # match ne marche que pour Python 3.10 ou ultérieure
        # Distinction des différents cas de produits avec leur id
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
        """ Permet de trouver le multiplier associé à un poids"""
        match id:
            case 7:
                return 1000000.
            case 8:
                return 10**9.
            case 9:
                return 907185.
            case 41:
                return 907.185

