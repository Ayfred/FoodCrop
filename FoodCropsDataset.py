import enum

import pandas
#import tqdm as tqdm
from FoodCropFactory import FoodCropFactory
from IndicatorGroup import IndicatorGroup
from Unit import Unit


class FoodCropsDataset:
## On instancie dans le constructeur un tableau dans lequel on va stocker nos données
## On crée des ensembles pour collecter les données d'IndicatorGroup, commodityGroup, Unit, commodityType

    def __init__(self):
        self.tableau = []
        self.commodityGroup = {}
        self.indicatorGroup = {}
        self.geographicalLocation = {}
        self.unit = {}
        self.fcf = FoodCropFactory()

## La méthode load permet de charger depuis le fichier Excel les colonnes de données associées aux paramètres utilisés
    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath)
        i = 0
        for index, row in dataframe.iterrows():#row commence à 1 donc imax = 16 si il y a 17 lignes sur excel

            commodity = self.fcf.createCommodity(int(row[7]), str(row[8]))
            unit = self.fcf.createUnit(int(row[11]), row[12])
            indicator = self.fcf.createIndicator(row[0], row[14], row[15], row[6], IndicatorGroup(int(row[0])), unit)
            measurement = self.fcf.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.tableau.append(measurement)

            addDict(indicator.id, measurement, self.indicatorGroup)
            addDict(str(row[2]), measurement, self.commodityGroup)#ok
            addDict(indicator.unit.id, measurement, self.unit)#ok
            addDict(str(row[4]), measurement, self.geographicalLocation)#ok
            ## On implémente un compteur i qui fait arrêter la boucle au bout de 5 itérations, afin de récupérer un nombre suffisant et pas trop important de données
            i += 1
            if i == 16: break
        print(self.tableau)


def addDict(key, value, dict):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

    def findMeasurements(self, commodityGroupId = None, indicatorGroupId = None, geographicalLocationId = None, unitId = None):
        result = []
        if commodityGroupId != None :
            result += self.commodityGroup[commodityGroupId]
        else:
            if indicatorGroupId != None :
                result += self.indicatorGroup[indicatorGroupId]
            else:
                if geographicalLocationId != None :
                    result += self.geographicalLocation[geographicalLocationId]
                else:
                    if unitId != None :
                        result += self.commodityGroup[unitId]
        if indicatorGroupId != None :
            merge(result, self.indicatorGroup[indicatorGroupId])
        if geographicalLocationId != None :
            merge(result, self.geographicalLocation[geographicalLocationId])
        if unitId != None :
            merge(result, self.commodityGroup[unitId])
        return result


def merge(l, m):
    r = []
    for x in l:
        if x in m:
            r.append(x)
    return r




