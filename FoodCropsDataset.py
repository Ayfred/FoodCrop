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
        self.unitGroup = {}
        self.commodityType = dict()
        self.fcf = FoodCropFactory()


## La méthode load permet de charger depuis le fichier Excel les colonnes de données associées aux paramètres utilisés
    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath)
        i = 0
        for index, row in tqdm.tqdm(dataframe.iterrows()):
            commodity = self.fcf.createCommodity(str(row[7]), str(row[8]))
            ## On additionne les chaînes de caractères des colonnes 4 et 14 afin de constituer une clé primaire pour les indicateurs
            unit = self.fcf.createUnit(row[11], row[12])
            indicator = self.fcf.createIndicator(row[0], row[14], row[15], row[6], IndicatorGroup, unit)
            measurement = self.fcf.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.Tableau.append(measurement)
            self.addDict(self.indicatorGroup, indicator.id, measurement)
            self.addDict(self.commodityGroup, row[2], measurement)
            self.addDict(self.unitGroup, indicator.unit.id, measurement)
            self.addDict(self.geographicalLocation, row[4], measurement)
            ## On implémente un compteur i qui fait arrêter la boucle au bout de 5 itérations, afin de récupérer un nombre suffisant et pas trop important de données
            i += 1
            if i == 5: break
        print(self.commodityType)
        print(self.indicatorGroup)
        print(self.Tableau)


# Permet d'ajouter des mesures aux dictionnaires, en vérifiant si la liste associé à l'id existe déjà
    def addDict(self, dict, id, measure):
        if id in dict:
            dict[id] += [measure]
        else:
            dict[id] = [measure]

## En cours de construction
    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        pass



