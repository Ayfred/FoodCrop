import enum

import pandas
import tqdm as tqdm

from Commodity import Commodity
from FoodCropFactory import FoodCropFactory
from IndicatorGroup import IndicatorGroup


class FoodCropsDataset:
## On instancie dans le constructeur un tableau dans lequel on va stocker nos données
## On crée des ensembles pour collecter les données d'IndicatorGroup, commodityGroup, Unit, commodityType

    def __init__(self):
        self.Tableau = []
        self.commodityGroup = {}
        self.indicatorGroup = {}
        self.geographicalLocation = {}
        self.unit = {}
        self.commodityType = dict()
        self.fcf = FoodCropFactory()

## La méthode load permet de charger depuis le fichier Excel les colonnes de données associées aux paramètres utilisés
    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath)
        i = 0
        for index, row in tqdm.tqdm(dataframe.iterrows()):
            commodity = self.fcf.createCommodity(str(row[7]), str(row[8]))
            ## On additionne les chaînes de caractères des colonnes 4 et 14 afin de constituer une clé primaire pour les indicateurs
            indicator = self.fcf.createIndicator(str(row[4])+str(row[14]), row[14], row[15], row[6], IndicatorGroup)
            measurement = self.fcf.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.Tableau.append(measurement)
            self.indicatorGroup[indicator.id] = measurement
            self.commodityGroup[str(row[2])] = measurement
            self.unit[indicator.unit.id] = measurement
            self.geographicalLocation[str(row[4])] = measurement
            ## On implémente un compteur i qui fait arrêter la boucle au bout de 5 itérations, afin de récupérer un nombre suffisant et pas trop important de données
            i += 1
            if i == 15: break
        print(self.commodityType)
        print(self.indicatorGroup)
        print(self.Tableau)
## En cours de construction
    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        pass




