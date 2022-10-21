import enum

import pandas

from FoodCropFactory import FoodCropFactory
from IndicatorGroup import IndicatorGroup


class FoodCropsDataset:

    def __init__(self):
        self.Tableau = []
        self.commodityGroup = {}
        self.indicatorGroup = {}
        self.geographicalLocation = {}
        self.unit = {}
        self.commodityType = dict()
        self.fcf = FoodCropFactory()
        self.load("FeedGrains.csv")

    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath)
        i = 0
        for index, row in dataframe.iterrows():
            commodity = self.fcf.createCommodity(str(row[7]), self.commodityType,str(row[8]))
            indicator = self.fcf.createIndicator(str(row[4]) + str(row[14]), row[14], row[15], row[6], IndicatorGroup,self.indicatorGroup)
            measurement = self.fcf.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.Tableau.append(measurement)
            i += 1
            if i == 5: break
        print(self.commodityType)
        print(self.indicatorGroup)
        print(self.Tableau)

    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        pass




