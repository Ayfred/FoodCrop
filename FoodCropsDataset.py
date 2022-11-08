import enum

import pandas
import tqdm as tqdm

from Commodity import Commodity
from CommodityGroup import CommodityGroup
from FoodCropFactory import FoodCropFactory
from IndicatorGroup import IndicatorGroup
from Unit import Unit


class FoodCropsDataset:
## On instancie dans le constructeur un tableau dans lequel on va stocker nos données
## On crée des ensembles pour collecter les données d'IndicatorGroup, commodityGroup, Unit, commodityType

    def __init__(self):
        self.tableau = set()
        self.commodityGroup = {}
        self.indicatorGroup = {}
        self.geographicalLocation = {}
        self.unitGroup = {}
        self.fcf = FoodCropFactory()


## La méthode load permet de charger depuis le fichier Excel les colonnes de données associées aux paramètres utilisés
    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath)
        for index, row in dataframe.iterrows():#row commence à 1 donc imax = 16 si il y a 17 lignes sur excel

            commodity = self.fcf.createCommodity(CommodityGroup(self.commodityGrp(row[2])), int(row[7]), str(row[8]))
            unit = self.fcf.createUnit(int(row[11]), row[12])
            indicator = self.fcf.createIndicator(row[0], row[14], row[15], row[6], IndicatorGroup(int(row[0])), unit)
            measurement = self.fcf.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.tableau.add(measurement)

            self.addDict(indicator.id, measurement, self.indicatorGroup)
            print(index)
            self.addDict(self.commodityGrp(row[2]), measurement, self.commodityGroup)#ok
            self.addDict(indicator.unit.id, measurement, self.unit)#ok
            self.addDict(int(row[4]), measurement, self.geographicalLocation)#ok

# Permet d'ajouter des mesures aux dictionnaires, en vérifiant si la liste associé à l'id existe déjà
    def addDict(self, key, value, dict):
        if key not in dict:
            dict[key] = set()
        dict[key].add(value)

    def findMeasurements(self, commodityGroupId = None, indicatorGroupId = None, geographicalLocationId = None, unitId = None):
        result = {}
        if commodityGroupId is not None:
            result = self.commodityGroup[commodityGroupId]
            if indicatorGroupId is not None:
                result = result & self.indicatorGroup[indicatorGroupId]
            if geographicalLocationId is not None:
                result = result & self.geographicalLocation[geographicalLocationId]
            if unitId is not None:
                result = result & self.commodityGroup[unitId]
            return result
        elif indicatorGroupId is not None:
            result = self.indicatorGroup[indicatorGroupId]
            if geographicalLocationId is not None:
                result = result & self.geographicalLocation[geographicalLocationId]
            if unitId is not None:
                result = result & self.commodityGroup[unitId]
            return result
        elif geographicalLocationId is not None:
            result = self.geographicalLocation[geographicalLocationId]
            if unitId is not None:
                result = result & self.commodityGroup[unitId]
            return result
        elif unitId is not None:
            result = self.commodityGroup[unitId]
        else:
            return self.tableau

    def commodityGrp(self, id):
        if id is None :
            return CommodityGroup(21)
        else:
            return CommodityGroup(int(id))

def merge(l, m):
    r = []
    for x in l:
        if x in m:
            r.append(x)
    return r