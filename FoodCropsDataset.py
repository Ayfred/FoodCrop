import pandas

import FoodCropFactory
import IndicatorGroup
from CommodityGroup import CommodityGroup


class FoodCropsDataset:

    def __init__(self, CommodityGroup, FoodCropFactory):
        self.CommodityGroup = CommodityGroup
        self.foodcropfactory = FoodCropFactory
        self.commodityType = {}
        self.IndicatorGroup = {}
        self.geographicalLocation = {}
        self.unit = {}
        self.Tableau = []
        self.load("D:\maxim\Documents\Python\FeedGrains.csv")

    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath) #"D:\maxim\Documents\Python\FeedGrains.csv"

        for index, row in dataframe.iterrows():
            #print(index, row)
            commodity = self.foodcropfactory.FoodCropFactory.createCommodity(self.CommodityGroup, index, str(row[8]))
            print(commodity)
            indicator = self.foodcropfactory.FoodCropFactory.createIndicator(self.IndicatorGroup, index, row[14], row[15], row[6], IndicatorGroup)
            measurement = self.foodcropfactory.FoodCropFactory.createMeasurement(index, row[13], row[16], row[17], commodity, indicator)
            self.Tableau.append(measurement)
        print(self.Tableau)

    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        pass


fcf = FoodCropFactory()
cg = CommodityGroup()
test = FoodCropsDataset(cg, fcf)


