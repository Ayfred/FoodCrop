import pandas

from FoodCropsDataset import FoodCropsDataset

dataframe = pandas.read_csv("FeedGrains.csv")
fcd = FoodCropsDataset()
fcd.load("FeedGrains.csv")

result = fcd.findMeasurements( commodityGroupId = 17, indicatorGroupId = 1, geographicalLocationId = 1, unitId = 4)
for measurement in result:
    print(measurement.describe())

