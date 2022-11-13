import pandas

from FoodCropsDataset import FoodCropsDataset

## Chargement des données
dataframe = pandas.read_csv("FeedGrains.csv")
fcd = FoodCropsDataset()
fcd.load("FeedGrains.csv")

## On choisi les identifiants qu'on souhaite rechercher
result = fcd.findMeasurements( commodityGroupId = 17, indicatorGroupId = 1, geographicalLocationId = 1, unitId = 4)
for measurement in result:
    print(measurement.describe())

