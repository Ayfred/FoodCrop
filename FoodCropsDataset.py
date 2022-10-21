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
        dataframe = pandas.read_csv(datasetPath) #"D:\maxim\Documents\Python\FeedGrains.csv"
        i = 0
        for index, row in dataframe.iterrows():
            commodity = self.fcf.createCommodity(index, self.commodityType,str(row[8]))
            indicator = self.fcf.createIndicator(index, row[14], row[15], row[6], IndicatorGroup,self.indicatorGroup)
            measurement = self.fcf.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.Tableau.append(measurement)
            i += 1
            if i == 5: break
        print(self.Tableau)

    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        pass




