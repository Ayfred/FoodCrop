import pandas

from FoodCropsDataset import FoodCropsDataset

dataframe = pandas.read_csv("FeedGrains.csv")
fcd = FoodCropsDataset()
fcd.load("FeedGrains.csv")

result = fcd.findMeasurements(17, 1, 1, 4)
for measurement in result:
    print(measurement.describe())

