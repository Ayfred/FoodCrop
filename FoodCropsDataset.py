import pandas
from CommodityGroup import CommodityGroup
from FoodCropFactory import FoodCropFactory
from IndicatorGroup import IndicatorGroup

class FoodCropsDataset:
    ## On instancie dans le constructeur un tableau dans lequel on va stocker nos données et FoodCropFactory
    ## On crée des dictionnaires pour collecter les données d'indicatorGroup, commodityGroupDict, Unit et geographicalLocation

    def __init__(self):
        self.tableau = set()
        self.commodityGroupDict = {}
        self.indicatorGroup = {}
        self.geographicalLocation = {}
        self.unitGroup = {}
        self.fcf = FoodCropFactory()


    ## La méthode load permet de charger depuis le fichier Excel les colonnes de données associées aux paramètres utilisés
    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath)
        for index, row in dataframe.iterrows():

            commodity = self.fcf.createCommodity(CommodityGroup(self.findCommodityGroup(row[2])), int(row[7]), str(row[8]))
            unit = self.fcf.createUnit(int(row[11]), row[12])
            indicator = self.fcf.createIndicator(row[0], int(row[14]), row[15], row[6], IndicatorGroup(int(row[0])), unit)
            measurement = self.fcf.createMeasurement(index, int(row[13]), float(row[18]), int(row[16]), row[17], commodity, indicator)
            self.tableau.add(measurement)

            ## On remplit les dictionnaires
            self.addDict(indicator.id, measurement, self.indicatorGroup)
            self.addDict(self.findCommodityGroup(row[2]), measurement, self.commodityGroupDict)#ok
            self.addDict(unit.id, measurement, self.unitGroup)#ok
            self.addDict(int(row[4]), measurement, self.geographicalLocation)#ok



    # Permet d'ajouter des mesures aux dictionnaires, en vérifiant si la liste associé à l'id existe déjà
    def addDict(self, key, value, dict):
        if key not in dict:
            dict[key] = set()
        dict[key].add(value)

    #Méthode find Measurements
    def findMeasurements(self, commodityGroupId = None, indicatorGroupId = None, geographicalLocationId = None, unitId = None):
        result = {}
        if commodityGroupId is not None:
            result = self.commodityGroupDict[commodityGroupId]
            if indicatorGroupId is not None:
                result = result & self.indicatorGroup[indicatorGroupId]
            if geographicalLocationId is not None:
                result = result & self.geographicalLocation[geographicalLocationId]
            if unitId is not None:
                result = result & self.unitGroup[unitId]
            return result
        elif indicatorGroupId is not None:
            result = self.indicatorGroup[indicatorGroupId]
            if geographicalLocationId is not None:
                result = result & self.geographicalLocation[geographicalLocationId]
            if unitId is not None:
                result = result & self.unitGroup[unitId]
            return result
        elif geographicalLocationId is not None:
            result = self.geographicalLocation[geographicalLocationId]
            if unitId is not None:
                result = result & self.unitGroup[unitId]
            return result
        elif unitId is not None:
            result = self.unitGroup[unitId]

        return self.tableau

    def findCommodityGroup(self, id):
        try:
            intId = int(id)
            return intId
        except ValueError:
            return 21
