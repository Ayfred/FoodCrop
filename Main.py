import pandas

from FoodCropsDataset import FoodCropsDataset

## Chargement des données
dataframe = pandas.read_csv("FeedGrains.csv")
fcd = FoodCropsDataset()
fcd.load("FeedGrains.csv")


