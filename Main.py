import pandas

from CommodityGroup import CommodityGroup
from FoodCropsDataset import FoodCropsDataset

print(CommodityGroup)
dataframe = pandas.read_csv("FeedGrains.csv")
fcd = FoodCropsDataset()
fcd.load("FeedGrains.csv")
print(fcd.findMeasurements())

