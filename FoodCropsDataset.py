import enum

import pandas
from FoodCropFactory import FoodCropFactory
from IndicatorGroup import IndicatorGroup
from CommodityGroup import CommodityGroup


class FoodCropsDataset:

    def __init__(self):
        self.CommodityGroup = CommodityGroup
        self.FoodCropFactory = FoodCropFactory()
        self.commodityType = {}
        self.IndicatorGroup = {}
        self.geographicalLocation = {}
        self.unit = {}
        self.Tableau = []
        self.load("D:\maxim\Documents\Python\FeedGrains.csv")

    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath) #"D:\maxim\Documents\Python\FeedGrains.csv"
        i = 0
        for index, row in dataframe.iterrows():
            commodity = self.FoodCropFactory.createCommodity(index, str(row[8]))
            indicator = self.FoodCropFactory.createIndicator(index, row[14], row[15], row[6], IndicatorGroup)
            measurement = self.FoodCropFactory.createMeasurement(index, row[13], row[18], row[16], row[17], commodity, indicator)
            self.Tableau.append(measurement)
            i += 1
            if i == 5: break
        print(self.Tableau)

    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        pass


test = FoodCropsDataset()


