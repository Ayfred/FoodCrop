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
        for index, row in dataframe.iterrows():#row commence à 1 donc imax = 16 si il y a 17 lignes sur excel

            commodity = self.fcf.createCommodity(str(row[7]), str(row[8]))
            ## On additionne les chaînes de caractères des colonnes 4 et 14 afin de constituer une clé primaire pour les indicateurs
            unit = Unit(row[11], row[12])
            indicator = self.fcf.createIndicator(str(row[4])+str(row[11])+str(row[14]), row[14], row[15], row[6], IndicatorGroup, unit)
            measurement = self.fcf.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.Tableau.append(measurement)

            createDict(indicator.id, measurement, self.indicatorGroup)
            #self.indicatorGroup[indicator.id] = measurement

            createDict(str(row[2]), measurement, self.commodityGroup)#ok
            #self.commodityGroup[str(row[2])] = measurement

            createDict(indicator.unit.id, measurement, self.unit)#ok
            #self.unit[indicator.unit.id] = measurement

            createDict(str(row[4]), measurement, self.geographicalLocation)#ok
            #self.geographicalLocation[str(row[4])] = measurement

            ## On implémente un compteur i qui fait arrêter la boucle au bout de 5 itérations, afin de récupérer un nombre suffisant et pas trop important de données
            i += 1
            if i == 16: break

        #ok
        #print("geographical : ")
        #print(self.geographicalLocation)
        #print("size : "+ str(len(self.geographicalLocation)))
        #print("geographical : " + str(len(self.geographicalLocation['1.0'])))

        #print("unit : ")
        #print(self.unit)
        #print(len(self.unit))

        #print("commodity Group : ")
        #print(self.commodityGroup)
        #print(len(self.commodityGroup))
        #print("commidity : " + str(len(self.commodityGroup['17.0'])))


        #print("indicatorGroup : ")
        #print(self.indicatorGroup)
        #print(len(self.indicatorGroup))

        #ok
        #print("Tableau : ")
        #print(self.Tableau)
        #print(len(self.Tableau))



def createDict(key, value, dict):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)






## En cours de construction
    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        pass




