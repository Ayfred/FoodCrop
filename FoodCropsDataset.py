import pandas
import FoodCropFactory
import Measurement
from Unit import Unit


class FoodCropsDataset:

    dataframe = str
    factory = FoodCropFactory

    def __init__(self):
        self.factory


    def load(self, datasetPath : str):
        dataframe = pandas.read_csv(datasetPath) #"D:\maxim\Documents\Python\FeedGrains.csv"
        return dataframe


    def findMeasurements(self, commodityType, IndicatorGroup, geographicalLocation, unit):
        commodityType = None
        IndicatorGroup  = None
        geographicalLocation = None
        return None # List[Measurements]




