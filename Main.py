import pandas

from FoodCropsDataset import FoodCropsDataset

dataframe = pandas.read_csv("FeedGrains.csv")
fcd = FoodCropsDataset()
fcd.load("FeedGrains.csv")


