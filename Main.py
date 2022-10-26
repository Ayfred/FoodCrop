import pandas

from CommodityGroup import CommodityGroup
from FoodCropsDataset import FoodCropsDataset

print(CommodityGroup["OATS"])
dataframe = pandas.read_csv("FeedGrains.csv")
fcd = FoodCropsDataset()
fcd.load("FeedGrains.csv")

