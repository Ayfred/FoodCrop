import pandas
import FoodCropFactory
import Measurement
from Unit import Unit


class FoodCropsDataset:

    dataframe = str
    factory = FoodCropFactory

    def __init__(self):
        self.factory


    def load(self, datasetPath):
        dataframe = pandas.read_csv(datasetPath) #"D:\maxim\Documents\Python\FeedGrains.csv"

        for index, row in dataframe.iterrows():
            column_value = row['R']





    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        return None # List[Measurements]




